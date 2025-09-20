'use client';

import React, { useState } from 'react';
import { useApi } from '@/contexts/ApiContext';
import { useSession } from 'next-auth/react';

export default function ProductsPage() {
  const { products, loading, error, addToCart, fetchProducts } = useApi();
  const { data: session } = useSession();
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<number | null>(null);

  const handleSearch = () => {
    fetchProducts({ search: searchTerm, category: selectedCategory });
  };

  const handleAddToCart = (productId: number) => {
    if (!session) {
      alert('Please log in to add items to cart');
      return;
    }
    addToCart(productId, 1);
  };

  if (loading.products) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-lg">Loading products...</div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold text-gray-900">Products</h1>
        <div className="flex space-x-4">
          <input
            type="text"
            placeholder="Search products..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
          />
          <button
            onClick={handleSearch}
            className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors"
          >
            Search
          </button>
        </div>
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
          {error}
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {products.map((product) => (
          <div key={product.id} className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
            <div className="h-48 bg-gray-200 flex items-center justify-center">
              {product.images && product.images.length > 0 ? (
                <img
                  src={product.images[0].image}
                  alt={product.name}
                  className="w-full h-full object-cover"
                />
              ) : (
                <div className="text-gray-400 text-4xl">📦</div>
              )}
            </div>
            
            <div className="p-4">
              <h3 className="text-lg font-semibold text-gray-900 mb-2">{product.name}</h3>
              <p className="text-gray-600 text-sm mb-2 line-clamp-2">{product.description}</p>
              
              <div className="flex items-center justify-between mb-2">
                <span className="text-2xl font-bold text-indigo-600">₹{product.unit_price}</span>
                <span className="text-sm text-gray-500">SKU: {product.sku}</span>
              </div>
              
              <div className="text-sm text-gray-500 mb-3">
                <p>Manufacturer: {product.manufacturer || 'N/A'}</p>
                <p>Delivery: {product.delivery_time}</p>
                <p>Stock: {product.stock_quantity} units</p>
                {product.average_rating > 0 && (
                  <p>Rating: ⭐ {product.average_rating} ({product.total_reviews} reviews)</p>
                )}
              </div>
              
              <div className="flex space-x-2">
                <button
                  onClick={() => handleAddToCart(product.id)}
                  disabled={!session || product.stock_quantity === 0}
                  className="flex-1 bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
                >
                  {!session ? 'Login to Add' : product.stock_quantity === 0 ? 'Out of Stock' : 'Add to Cart'}
                </button>
                <button className="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors">
                  View
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>

      {products.length === 0 && !loading.products && (
        <div className="text-center py-12">
          <div className="text-gray-400 text-6xl mb-4">📦</div>
          <h3 className="text-lg font-medium text-gray-900 mb-2">No products found</h3>
          <p className="text-gray-500">Try adjusting your search criteria</p>
        </div>
      )}
    </div>
  );
}
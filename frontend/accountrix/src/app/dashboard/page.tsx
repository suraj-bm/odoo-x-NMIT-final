'use client';

import React from 'react';
import { useApi } from '@/contexts/ApiContext';
import { useSession } from 'next-auth/react';

export default function DashboardPage() {
  const { categories, products, cart, orders, analytics, loading, error } = useApi();
  const { data: session } = useSession();

  const stats = [
    {
      name: 'Total Products',
      value: products.length,
      icon: '📦',
      color: 'bg-blue-500',
    },
    {
      name: 'Categories',
      value: categories.length,
      icon: '🏷️',
      color: 'bg-green-500',
    },
    {
      name: 'Cart Items',
      value: cart.length,
      icon: '🛒',
      color: 'bg-yellow-500',
    },
    {
      name: 'Orders',
      value: orders.length,
      icon: '📋',
      color: 'bg-purple-500',
    },
  ];

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
        <div className="text-sm text-gray-500">
          Welcome back, {session?.user?.name || 'Guest'}!
        </div>
      </div>

      {/* Connection Status */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">Backend Connection Status</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="flex items-center space-x-3">
            <div className={`w-3 h-3 rounded-full ${error ? 'bg-red-500' : 'bg-green-500'}`}></div>
            <span className="text-sm font-medium">
              {error ? 'Connection Error' : 'Connected to Backend'}
            </span>
          </div>
          <div className="text-sm text-gray-500">
            API URL: {process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api'}
          </div>
        </div>
        {error && (
          <div className="mt-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded">
            {error}
          </div>
        )}
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat) => (
          <div key={stat.name} className="bg-white rounded-lg shadow-md p-6">
            <div className="flex items-center">
              <div className={`w-12 h-12 ${stat.color} rounded-lg flex items-center justify-center text-white text-2xl`}>
                {stat.icon}
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">{stat.name}</p>
                <p className="text-2xl font-bold text-gray-900">
                  {loading.products || loading.categories || loading.cart || loading.orders ? '...' : stat.value}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Recent Products */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">Recent Products</h2>
        {loading.products ? (
          <div className="text-center py-8">
            <div className="text-lg">Loading products...</div>
          </div>
        ) : products.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {products.slice(0, 6).map((product) => (
              <div key={product.id} className="border border-gray-200 rounded-lg p-4">
                <h3 className="font-semibold text-gray-900">{product.name}</h3>
                <p className="text-sm text-gray-600 mt-1">{product.description}</p>
                <p className="text-indigo-600 font-semibold mt-2">₹{product.unit_price}</p>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center py-8 text-gray-500">
            No products available
          </div>
        )}
      </div>

      {/* Analytics */}
      {analytics && (
        <div className="bg-white rounded-lg shadow-md p-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">E-commerce Analytics</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="text-center">
              <p className="text-2xl font-bold text-indigo-600">{analytics.summary?.total_orders || 0}</p>
              <p className="text-sm text-gray-600">Total Orders</p>
            </div>
            <div className="text-center">
              <p className="text-2xl font-bold text-green-600">₹{analytics.summary?.total_revenue || 0}</p>
              <p className="text-sm text-gray-600">Total Revenue</p>
            </div>
            <div className="text-center">
              <p className="text-2xl font-bold text-purple-600">₹{analytics.summary?.net_profit || 0}</p>
              <p className="text-sm text-gray-600">Net Profit</p>
            </div>
          </div>
        </div>
      )}

      {/* Quick Actions */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">Quick Actions</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <a
            href="/products"
            className="flex items-center p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <div className="w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center text-indigo-600 text-xl">
              📦
            </div>
            <div className="ml-4">
              <p className="font-semibold text-gray-900">Browse Products</p>
              <p className="text-sm text-gray-600">View all available products</p>
            </div>
          </a>
          
          <a
            href="/cart"
            className="flex items-center p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <div className="w-10 h-10 bg-yellow-100 rounded-lg flex items-center justify-center text-yellow-600 text-xl">
              🛒
            </div>
            <div className="ml-4">
              <p className="font-semibold text-gray-900">View Cart</p>
              <p className="text-sm text-gray-600">{cart.length} items in cart</p>
            </div>
          </a>
          
          <a
            href="/reports"
            className="flex items-center p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <div className="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center text-green-600 text-xl">
              📊
            </div>
            <div className="ml-4">
              <p className="font-semibold text-gray-900">View Reports</p>
              <p className="text-sm text-gray-600">Analytics and insights</p>
            </div>
          </a>
        </div>
      </div>
    </div>
  );
}
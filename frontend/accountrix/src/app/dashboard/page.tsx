'use client';

import React from 'react';
import Sidebar from '@/components/sidebar';
import { kpiData, manufacturingOrders } from '@/data/dashboardData';

const statusColors: Record<string, string> = {
  'Planned': 'bg-gray-100 text-gray-800',
  'In Progress': 'bg-blue-100 text-blue-700',
  'Completed': 'bg-green-100 text-green-700',
  'Delayed': 'bg-red-100 text-red-700',
};

export default function DashboardPage() {
  return (
    <div className="flex h-screen bg-gray-50 font-sans">
      <Sidebar activePage="dashboard" />

      <main className="flex-1 p-8 overflow-y-auto">
        <header className="pb-6">
          <h1 className="text-3xl font-bold text-gray-800">Manufacturing Dashboard</h1>
          <p className="text-gray-600">Monitor all manufacturing orders and production KPIs</p>
        </header>

        {/* KPI Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <div className="bg-white p-6 rounded-lg shadow-sm">
            <h3 className="text-sm font-medium text-gray-500">Total Orders</h3>
            <p className="text-3xl font-bold text-gray-800 mt-2">{kpiData.totalOrders}</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-sm">
            <h3 className="text-sm font-medium text-gray-500">In Progress</h3>
            <p className="text-3xl font-bold text-blue-600 mt-2">{kpiData.inProgress}</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-sm">
            <h3 className="text-sm font-medium text-gray-500">Completed</h3>
            <p className="text-3xl font-bold text-green-600 mt-2">{kpiData.completed}</p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-sm">
            <h3 className="text-sm font-medium text-gray-500">Delayed</h3>
            <p className="text-3xl font-bold text-red-600 mt-2">{kpiData.delayed}</p>
          </div>
        </div>

        {/* Manufacturing Orders Table */}
        <div className="bg-white rounded-lg shadow-sm p-6">
          <h3 className="font-semibold text-gray-700 mb-4">Manufacturing Orders</h3>
          <table className="w-full text-left">
            <thead>
              <tr className="text-gray-600">
                <th className="py-3 px-4">MO ID</th>
                <th className="py-3 px-4">Product</th>
                <th className="py-3 px-4">Quantity</th>
                <th className="py-3 px-4">Status</th>
                <th className="py-3 px-4">Start Date</th>
                <th className="py-3 px-4">End Date</th>
              </tr>
            </thead>
            <tbody className="text-gray-700">
              {manufacturingOrders.map((mo) => (
                <tr key={mo.id} className="border-t">
                  <td className="py-4 px-4 font-medium">{mo.id}</td>
                  <td className="py-4 px-4">{mo.product}</td>
                  <td className="py-4 px-4">{mo.qty}</td>
                  <td className="py-4 px-4">
                    <span className={`px-2 py-1 text-xs font-semibold rounded-full ${statusColors[mo.status]}`}>
                      {mo.status}
                    </span>
                  </td>
                  <td className="py-4 px-4">{mo.startDate}</td>
                  <td className="py-4 px-4">{mo.endDate}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </div>
  );
}

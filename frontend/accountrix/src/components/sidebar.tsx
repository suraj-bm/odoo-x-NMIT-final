'use client';

import React from 'react';
import { useSession, signIn, signOut } from "next-auth/react";

// Define the props for the Sidebar component
interface SidebarProps {
  activePage: 'dashboard' | 'contacts' | 'products' | 'taxes' | 'accounts' | 'purchases' | 'sales' | 'reports';
}

// Reusable Sidebar component
const Sidebar: React.FC<SidebarProps> = ({ activePage }) => {
  const { data: session, status } = useSession();

  // Helper function to determine the classes for the links
  const getLinkClassName = (page: SidebarProps['activePage']) => {
    return `flex items-center px-4 py-2.5 text-gray-600 rounded-lg hover:bg-gray-100 transition-colors duration-200 ${
      activePage === page ? 'bg-indigo-50 text-indigo-600' : ''
    }`;
  };

  return (
    <aside className="w-64 bg-white shadow-sm flex flex-col h-full">
      <div className="p-6 text-2xl font-bold text-gray-800 border-b">
        Accountix
      </div>

      {/* --- NAVIGATION --- */}
      <nav className="flex-1 px-4 py-6 space-y-4">
        {/* Main Section */}
        <div>
          <span className="px-4 text-xs font-semibold text-gray-500 uppercase tracking-wider">Main</span>
          <div className="mt-2 space-y-1">
            <a href="/dashboard" className={getLinkClassName('dashboard')}>Dashboard</a>
            <a href="/contacts" className={getLinkClassName('contacts')}>Contacts</a>
          </div>
        </div>

        {/* Transactions Section */}
        <div>
          <span className="px-4 text-xs font-semibold text-gray-500 uppercase tracking-wider">Transactions</span>
          <div className="mt-2 space-y-1">
            <a href="/products" className={getLinkClassName('products')}>Products</a>
            <a href="/purchases" className={getLinkClassName('purchases')}>Purchases</a>
            <a href="/sales" className={getLinkClassName('sales')}>Sales</a>
          </div>
        </div>

        {/* Configuration Section */}
        <div>
          <span className="px-4 text-xs font-semibold text-gray-500 uppercase tracking-wider">Configuration</span>
          <div className="mt-2 space-y-1">
            <a href="/taxes" className={getLinkClassName('taxes')}>Taxes</a>
            <a href="/accounts" className={getLinkClassName('accounts')}>Chart of Accounts</a>
            <a href="/reports" className={getLinkClassName('reports')}>Reports</a>
          </div>
        </div>
      </nav>

      {/* --- USER PROFILE SECTION --- */}
      <div className="p-4 border-t">
        {status === "authenticated" ? (
          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <img
                className="w-10 h-10 rounded-full"
                src={session.user?.image || "https://i.pravatar.cc/150?u=default"}
                alt="User Avatar"
              />
              <div className="ml-3">
                <p className="text-sm font-medium text-gray-800">{session.user?.name}</p>
                <p className="text-xs text-gray-500">{session.user?.email}</p>
              </div>
            </div>
            <button
              onClick={() => signOut()}
              className="ml-3 px-3 py-1 text-xs bg-red-500 text-white rounded"
            >
              Sign out
            </button>
          </div>
        ) : (
          <button
            onClick={() => signIn("google")}
            className="w-full px-3 py-2 text-sm bg-indigo-600 text-white rounded"
          >
            Sign in
          </button>
        )}
      </div>
    </aside>
  );
};

export default Sidebar;

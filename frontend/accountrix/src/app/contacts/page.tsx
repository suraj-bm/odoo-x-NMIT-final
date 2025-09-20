'use client';

import React from 'react';
import Link from 'next/link';

// Mock data for contacts
const contacts = [
    {
        id: 1,
        name: 'Nimesh Pathak',
        type: 'Customer',
        email: 'nimesh.p@example.com',
        phone: '9876543210',
        img: 'https://i.pravatar.cc/150?u=a042581f4e29026704a'
    },
    {
        id: 2,
        name: 'Azure Furniture',
        type: 'Vendor',
        email: 'contact@azurefurniture.com',
        phone: '8765432109',
        img: 'https://i.pravatar.cc/150?u=a042581f4e29026704b'
    },
    {
        id: 3,
        name: 'Rohan Sharma',
        type: 'Customer',
        email: 'rohan.s@example.com',
        phone: '7654321098',
        img: 'https://i.pravatar.cc/150?u=a042581f4e29026704c'
    },
    {
        id: 4,
        name: 'Royal Oak',
        type: 'Vendor',
        email: 'sales@royaloak.com',
        phone: '6543210987',
        img: 'https://i.pravatar.cc/150?u=a042581f4e29026704d'
    },
    {
        id: 5,
        name: 'Greenwood Inc.',
        type: 'Both',
        email: 'support@greenwood.com',
        phone: '5432109876',
        img: 'https://i.pravatar.cc/150?u=a042581f4e29026704e'
    }
];

// This is the main component for the contacts page.
const ContactsPage = () => {
    return (
        <div className="flex h-screen bg-gray-100 font-sans">
            {/* Sidebar */}
            <aside className="w-64 bg-white shadow-md flex flex-col">
                <div className="p-6 text-2xl font-bold text-gray-800 border-b">
                    Shiv Accounts
                </div>
                <nav className="flex-1 px-4 py-6 space-y-2">
                    <Link href="/dashboard" className="flex items-center px-4 py-2 text-gray-700 rounded-md hover:bg-gray-200">
                        <svg className="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" /></svg>
                        Dashboard
                    </Link>
                    <Link href="/contacts" className="flex items-center px-4 py-2 text-gray-700 bg-gray-200 rounded-md">
                        <svg className="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M15 21a6 6 0 00-9-5.197m0 0A5.995 5.995 0 0112 13a5.995 5.995 0 013 5.197M15 21a6 6 0 00-9-5.197" /></svg>
                        Contacts
                    </Link>
                    <Link href="/products" className="flex items-center px-4 py-2 text-gray-700 rounded-md hover:bg-gray-200">
                       <svg className="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4" /></svg>
                        Products
                    </Link>
                    <Link href="/taxes" className="flex items-center px-4 py-2 text-gray-700 rounded-md hover:bg-gray-200">
                        <svg className="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 14l6-6m-5.5.5h.01m4.99 5h.01M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16l3.5-2 3.5 2 3.5-2 3.5 2z" /></svg>
                        Taxes
                    </Link>
                    <Link href="/accounts" className="flex items-center px-4 py-2 text-gray-700 rounded-md hover:bg-gray-200">
                       <svg className="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V7a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
                        Chart of Accounts
                    </Link>
                    <Link href="/purchases" className="flex items-center px-4 py-2 text-gray-700 rounded-md hover:bg-gray-200">
                        <svg className="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" /></svg>
                        Purchase Orders
                    </Link>
                    <Link href="/sales" className="flex items-center px-4 py-2 text-gray-700 rounded-md hover:bg-gray-200">
                        <svg className="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" /></svg>
                        Sales Orders
                    </Link>
                     <Link href="/reports" className="flex items-center px-4 py-2 text-gray-700 rounded-md hover:bg-gray-200">
                        <svg className="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>
                        Reports
                    </Link>
                </nav>
            </aside>

            {/* Main content */}
            <main className="flex-1 p-8 overflow-y-auto">
                <header className="flex items-center justify-between pb-6 border-b">
                    <div>
                        <h1 className="text-3xl font-bold text-gray-800">Contacts</h1>
                        <p className="text-gray-600">Manage your customers and vendors</p>
                    </div>
                    <div className="flex items-center space-x-4">
                        <div className="relative">
                            <input type="text" placeholder="Search contacts..." className="px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500" />
                        </div>
                         <button className="px-4 py-2 font-medium text-white bg-indigo-600 rounded-md hover:bg-indigo-700">
                            + New Contact
                        </button>
                    </div>
                </header>

                {/* Contacts Table */}
                <div className="mt-8 bg-white rounded-lg shadow-md">
                     <div className="p-6">
                        <table className="w-full text-left">
                            <thead>
                                <tr className="text-gray-600">
                                    <th className="py-3 px-4">Name</th>
                                    <th className="py-3 px-4">Type</th>
                                    <th className="py-3 px-4">Email</th>
                                    <th className="py-3 px-4">Phone</th>
                                    <th className="py-3 px-4">Actions</th>
                                </tr>
                            </thead>
                            <tbody className="text-gray-700">
                                {contacts.map((contact, index) => (
                                    <tr key={contact.id} className={index % 2 === 0 ? '' : 'bg-gray-50'}>
                                        <td className="py-4 px-4 flex items-center">
                                            <img src={contact.img} alt={contact.name} className="w-10 h-10 rounded-full mr-4" />
                                            <span className="font-medium">{contact.name}</span>
                                        </td>
                                        <td className="py-4 px-4">
                                            <span className={`px-2 py-1 text-xs font-semibold rounded-full ${
                                                contact.type === 'Customer' ? 'bg-blue-100 text-blue-700' :
                                                contact.type === 'Vendor' ? 'bg-purple-100 text-purple-700' :
                                                'bg-gray-200 text-gray-800'
                                            }`}>
                                                {contact.type}
                                            </span>
                                        </td>
                                        <td className="py-4 px-4">{contact.email}</td>
                                        <td className="py-4 px-4">{contact.phone}</td>
                                        <td className="py-4 px-4">
                                            <button className="text-indigo-600 hover:text-indigo-900 mr-4">Edit</button>
                                            <button className="text-red-600 hover:text-red-900">Delete</button>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </main>
        </div>
    );
};

export default ContactsPage;


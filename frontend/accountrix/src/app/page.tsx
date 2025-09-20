'use client';

import React from 'react';
import { useSession, signIn, signOut } from "next-auth/react";
import LoginForm from '@/components/LoginForm';

const Home = () => {
    const { data: session, status } = useSession();

    // Show login form if not authenticated
    if (status === "unauthenticated") {
        return <LoginForm />;
    }

    // Helper component for feature cards
    const Feature = ({ icon, title, description }: { icon: React.ReactNode, title: string, description: string }) => (
        <div className="bg-white p-6 rounded-lg shadow-sm text-center">
            <div className="flex justify-center items-center mb-4 text-indigo-600">
                {icon}
            </div>
            <h3 className="text-xl font-bold text-gray-800 mb-2">{title}</h3>
            <p className="text-gray-600">{description}</p>
        </div>
    );

    return (
        <div className="bg-gray-50 font-sans">
            {/* Header */}
            <header className="bg-white shadow-sm sticky top-0 z-50">
                <div className="container mx-auto px-6 py-4 flex justify-between items-center">
                    <h1 className="text-2xl font-bold text-gray-800">Accountix</h1>
                    
                    {/* Right Side Navigation */}
                    <div>
                        {status === "authenticated" ? (
                            <div className="flex items-center space-x-4">
                                <img
                                    src={session.user?.image || "https://i.pravatar.cc/150?u=default"}
                                    alt="User Avatar"
                                    className="w-10 h-10 rounded-full"
                                />
                                <span className="text-gray-700">{session.user?.name}</span>
                                <button
                                    onClick={() => signOut()}
                                    className="bg-red-500 text-white font-semibold py-2 px-4 rounded-lg hover:bg-red-600 transition-colors"
                                >
                                    Sign Out
                                </button>
                            </div>
                        ) : (
                            <div className="flex items-center space-x-4">
                                <button
                                    onClick={() => signIn()}
                                    className="text-gray-600 hover:text-indigo-600"
                                >
                                    Login
                                </button>
                                <button
                                    onClick={() => signIn('google')}
                                    className="bg-white text-gray-700 font-semibold py-2 px-4 rounded-lg border border-gray-300 hover:bg-gray-50 transition-colors flex items-center"
                                >
                                    <svg className="w-5 h-5 mr-2" viewBox="0 0 24 24">
                                        <path
                                            fill="currentColor"
                                            d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
                                        />
                                        <path
                                            fill="currentColor"
                                            d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
                                        />
                                        <path
                                            fill="currentColor"
                                            d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"
                                        />
                                        <path
                                            fill="currentColor"
                                            d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
                                        />
                                    </svg>
                                    Google
                                </button>
                                <a
                                    href="#"
                                    className="bg-indigo-600 text-white font-semibold py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors"
                                >
                                    Sign Up
                                </a>
                            </div>
                        )}
                    </div>
                </div>
            </header>

            {/* Hero Section */}
            <main>
                <section className="text-center py-20 bg-white">
                    <div className="container mx-auto px-6">
                        <h2 className="text-4xl md:text-5xl font-extrabold text-gray-800 mb-4">
                            Modern Accounting, Simplified
                        </h2>
                        <p className="text-lg text-gray-600 max-w-2xl mx-auto mb-8">
                            Accountix helps you manage your finances effortlessly with intuitive tools for invoicing, expense tracking, and real-time reporting.
                        </p>
                        <a
                            href="#"
                            className="bg-indigo-600 text-white font-semibold py-3 px-8 rounded-lg hover:bg-indigo-700 transition-colors text-lg"
                        >
                            Get Started for Free
                        </a>
                    </div>
                </section>

                {/* Features Section */}
                <section id="features" className="py-20">
                    <div className="container mx-auto px-6">
                        <div className="text-center mb-12">
                            <h2 className="text-3xl font-bold text-gray-800">Everything You Need to Run Your Business</h2>
                            <p className="text-gray-600">Powerful features to streamline your financial workflow.</p>
                        </div>
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                            <Feature
                                icon={<svg className="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" /></svg>}
                                title="Easy Invoicing"
                                description="Create and send professional invoices in minutes. Track payments and send reminders automatically."
                            />
                            <Feature
                                icon={<svg className="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>}
                                title="Real-Time Reports"
                                description="Generate balance sheets, profit & loss statements, and inventory reports with a single click."
                            />
                            <Feature
                                icon={<svg className="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" /></svg>}
                                title="Manage Purchases"
                                description="Easily create purchase orders, convert them to bills, and track your payables."
                            />
                        </div>
                    </div>
                </section>
                
                {/* CTA Section */}
                <section className="bg-indigo-600 text-white">
                    <div className="container mx-auto px-6 py-16 text-center">
                        <h2 className="text-3xl font-bold mb-3">Ready to Take Control of Your Finances?</h2>
                        <p className="max-w-xl mx-auto mb-6">Join hundreds of businesses simplifying their accounting with Accountix.</p>
                        <a
                            href="#"
                            className="bg-white text-indigo-600 font-semibold py-3 px-8 rounded-lg hover:bg-gray-100 transition-colors text-lg"
                        >
                            Start Your Free Trial
                        </a>
                    </div>
                </section>
            </main>

            {/* Footer */}
            <footer className="bg-white">
                <div className="container mx-auto px-6 py-8">
                    <div className="flex justify-between items-center">
                        <p className="text-gray-600">&copy; 2025 Shiv Accounts. All rights reserved.</p>
                        <div className="flex space-x-4">
                            <a href="#" className="text-gray-600 hover:text-indigo-600">Privacy Policy</a>
                            <a href="#" className="text-gray-600 hover:text-indigo-600">Terms of Service</a>
                        </div>
                    </div>
                </div>
            </footer>
        </div>
    );
};

export default Home;

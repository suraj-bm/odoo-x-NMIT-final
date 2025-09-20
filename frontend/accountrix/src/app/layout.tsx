import './globals.css'
import Sidebar from '@/components/sidebar' // adjust path
import Providers from '@/hooks/providers'
export const metadata = {
  title: 'Shiv Accounts',
  description: 'Admin Dashboard',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
          <Providers>
        <div className="flex h-screen bg-gray-50 font-sans">
            
          <Sidebar activePage="dashboard" />
          <main className="flex-1 overflow-y-auto p-8">{children}</main>
        </div>
          </Providers>
      </body>
    </html>
  )
}

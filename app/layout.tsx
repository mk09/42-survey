import type { Metadata } from 'next';
import './globals.css';
export const metadata: Metadata = { title: 'Folio — Survey workspace', description: 'A thoughtful workspace for projects, surveys, and better questions.' };
export default function RootLayout({children}: Readonly<{children: React.ReactNode}>) { return <html lang="en"><body>{children}</body></html>; }

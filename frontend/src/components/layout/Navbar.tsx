import Link from 'next/link';

export default function Navbar() {
  return (
    <header className="sticky top-0 z-40 border-b border-violet-500/30 bg-violet-900/90 backdrop-blur">
      <nav className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <Link href="/" className="text-2xl font-bold">Preu AI</Link>
        <div className="hidden gap-6 text-sm md:flex">
          <a href="#incluye">¿Qué incluye?</a>
          <a href="#como-funciona">¿Cómo funciona?</a>
          <a href="#planes">Planes</a>
        </div>
        <Link href="/login" className="rounded-full bg-white/10 px-4 py-2 text-sm">Iniciar sesión</Link>
      </nav>
    </header>
  );
}

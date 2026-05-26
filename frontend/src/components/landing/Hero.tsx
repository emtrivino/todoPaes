import Link from 'next/link';

export default function Hero() {
  return (
    <section className="mx-auto grid max-w-6xl gap-10 px-6 py-16 md:grid-cols-2 md:py-20">
      <div>
        <span className="inline-block rounded-full bg-amber-400 px-4 py-2 text-sm font-bold text-violet-900">🔥 Semana Intensiva PAES</span>
        <h1 className="mt-6 text-5xl font-extrabold leading-tight md:text-6xl">Plan Intensivo PAES de Invierno</h1>
        <p className="mt-6 text-xl text-violet-200">Prepárate con acceso completo, mini clases, tutor IA y sesiones en vivo.</p>
        <Link href="/register" className="mt-8 inline-block rounded-2xl bg-white px-8 py-4 text-lg font-bold text-violet-900">Inscribirme ahora</Link>
      </div>
      <div className="rounded-3xl border border-violet-400/40 bg-violet-800/40 p-8">
        <p className="text-sm uppercase tracking-widest text-violet-300">+4.000 estudiantes</p>
        <p className="mt-4 text-3xl font-bold">Subieron su puntaje con Preu AI</p>
        <ul className="mt-6 space-y-3 text-violet-100">
          <li>✅ Ensayos PAES ilimitados</li>
          <li>✅ Tutor IA 24/7</li>
          <li>✅ Más de 400 mini clases</li>
          <li>✅ Semana intensiva en vivo</li>
        </ul>
      </div>
    </section>
  );
}

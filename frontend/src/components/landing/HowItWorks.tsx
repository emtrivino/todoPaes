export default function HowItWorks() {
  return (
    <section id="como-funciona" className="mx-auto max-w-6xl px-6 py-16">
      <h2 className="text-center text-4xl font-bold">¿Cómo funciona?</h2>
      <div className="mt-8 grid gap-6 md:grid-cols-4">
        {['Accedes al plan', 'Practicas cada día', 'Semana intensiva', 'Rindes la PAES'].map((step, i) => (
          <div key={step} className="rounded-2xl border border-violet-400/40 bg-violet-800/30 p-5">
            <p className="text-sm text-violet-300">Paso {i + 1}</p>
            <p className="mt-2 text-xl font-semibold">{step}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

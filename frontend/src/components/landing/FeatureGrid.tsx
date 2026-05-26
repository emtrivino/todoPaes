const features = [
  'Sube tu puntaje con ensayos ilimitados',
  'Resuelve dudas con tutor IA 24/7',
  'Domina el temario con +400 mini clases',
  'Rankings y estadísticas en tiempo real',
  'Simuladores de postulación y carrera'
];

export default function FeatureGrid() {
  return (
    <section id="incluye" className="mx-auto max-w-6xl px-6 py-16">
      <h2 className="text-center text-4xl font-bold">¿Qué incluye el plan intensivo?</h2>
      <div className="mt-10 grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {features.map((f) => (
          <article key={f} className="rounded-2xl border border-violet-400/40 bg-violet-800/30 p-6">
            <p className="text-lg font-semibold">{f}</p>
          </article>
        ))}
      </div>
    </section>
  );
}

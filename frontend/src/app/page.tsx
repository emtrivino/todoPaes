import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';
import Hero from '../components/landing/Hero';
import FeatureGrid from '../components/landing/FeatureGrid';
import HowItWorks from '../components/landing/HowItWorks';
import ProductPreview from '../components/landing/ProductPreview';
import CTASection from '../components/landing/CTASection';

export default function HomePage() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-violet-900 via-violet-800 to-violet-950">
      <Navbar />
      <Hero />
      <ProductPreview />
      <FeatureGrid />
      <HowItWorks />
      <CTASection />
      <Footer />
    </main>
  );
}

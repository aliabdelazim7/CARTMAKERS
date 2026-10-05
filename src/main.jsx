import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import { ArrowUpRight, Check, ChevronRight, CircleCheck, Menu, X } from 'lucide-react';
import './styles.css';

const features = [
  ['01 / STOREFRONT', 'Mobile UX & catalog', 'Make product information, offers, trust, and navigation easier to understand and act on.'],
  ['02 / CHECKOUT', 'Payments & COD', 'Reduce friction across payment choice, confirmation, delivery, returns, and follow-up.'],
  ['03 / MEASUREMENT', 'Tracking & growth', 'Know what is working across ads, landing pages, conversion, CRM, and repeat purchase.']
];
const steps = [['01', 'Diagnose', 'Understand the business, demand, and current flow.'], ['02', 'Prioritize', 'Decide what changes first and what should wait.'], ['03', 'Build', 'Ship the agreed commerce and tracking work.'], ['04', 'Grow', 'Improve CRO, merchandising, CRM, and retention.']];

function App() {
  const [menu, setMenu] = useState(false);
  const [sent, setSent] = useState(false);
  const [error, setError] = useState('');
  const [busy, setBusy] = useState(false);

  async function submit(e) {
    e.preventDefault(); setBusy(true); setError('');
    const form = new FormData(e.currentTarget);
    try {
      const res = await fetch('/api/contact', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(Object.fromEntries(form)) });
      const data = await res.json();
      if (!res.ok || !data.ok) throw new Error(data.message || 'Please try again.');
      setSent(true); e.currentTarget.reset();
    } catch (err) { setError(err.message); } finally { setBusy(false); }
  }

  return <>
    <header className="nav shell">
      <a href="#top" className="brand"><img src="/assets/cartmakers-symbol.svg" /> <span>Cart<span>Makers</span></span></a>
      <button className="menu-toggle" onClick={() => setMenu(!menu)} aria-label="Toggle navigation">{menu ? <X/> : <Menu/>}</button>
      <nav className={menu ? 'nav-links open' : 'nav-links'}><a href="#work" onClick={() => setMenu(false)}>How it works</a><a href="#offer" onClick={() => setMenu(false)}>Readiness Sprint</a><a className="nav-cta" href="#contact" onClick={() => setMenu(false)}>Book a diagnostic <ArrowUpRight size={16}/></a></nav>
    </header>
    <main id="top">
      <section className="hero shell">
        <div className="hero-copy"><div className="eyebrow">ECOMMERCE SYSTEMS <i/> GROWTH</div><h1>We build<br/><em>stores that work.</em></h1><p className="lede">CartMakers helps growing brands turn demand from social and marketplaces into a commerce system that converts, tracks, and keeps improving.</p><div className="hero-actions"><a className="button primary" href="#contact">Book a Commerce Diagnostic <ArrowUpRight size={18}/></a><a className="text-link" href="#work">See how we work <ChevronRight size={17}/></a></div><div className="proof"><CircleCheck size={18}/><span>Egypt-first. GCC-ready. Built for real operations.</span></div></div>
        <div className="hero-panel"><div className="panel-label">THE COMMERCE FLOW <span>01—04</span></div><div className="flow"><div><b>01</b><span>Social demand</span><small>attention</small></div><div><b>02</b><span>Store & checkout</span><small>conversion</small></div><div><b>03</b><span>Payment & delivery</span><small>operations</small></div><div className="active"><b>04</b><span>Tracking & growth</span><small>repeat</small></div></div><div className="panel-foot"><span>One system. Fewer leaks.</span><span className="pulse"/></div></div>
      </section>
      <section className="section intro shell"><div className="section-kicker">THE REAL PROBLEM</div><div><h2>Your product may not<br/>be the problem.</h2><p>Demand gets lost when the catalog is unclear, the mobile experience is slow, checkout creates doubt, COD is unmanaged, tracking is incomplete, or nobody follows up after the order.</p></div></section>
      <section className="section shell" id="work"><div className="section-head"><div><div className="section-kicker">WHAT WE FIX</div><h2>Make every step<br/>of selling <em>work.</em></h2></div><p>We connect the pieces that turn online attention into a business you can actually operate.</p></div><div className="feature-grid">{features.map(([k,t,d]) => <article className="feature" key={k}><div className="section-kicker">{k}</div><h3>{t}</h3><p>{d}</p><ArrowUpRight className="feature-arrow" size={22}/></article>)}</div></section>
      <section className="section dark" id="offer"><div className="shell"><div className="section-head"><div><div className="section-kicker lime">THE FIRST STEP</div><h2>Clarity before<br/>a <em>big build.</em></h2></div><p>The Commerce Readiness Sprint finds where your customer journey is leaking, then turns the priorities into agreed implementation work.</p></div><div className="deliverables"><div><Check size={18}/> Current commerce journey review</div><div><Check size={18}/> Prioritized action backlog</div><div><Check size={18}/> Agreed implementation fixes</div><div><Check size={18}/> Tracking & measurement recommendations</div></div><a className="button lime-button" href="#contact">Start with the Readiness Sprint <ArrowUpRight size={18}/></a></div></section>
      <section className="section shell"><div className="section-kicker">HOW IT WORKS</div><h2>From leak to lift.</h2><div className="steps">{steps.map(([n,t,d]) => <div className="step" key={n}><span>{n}</span><h3>{t}</h3><p>{d}</p></div>)}</div></section>
      <section className="section contact shell" id="contact"><div className="contact-copy"><div className="section-kicker">LET'S TALK COMMERCE</div><h2>Find the leak before you rebuild the store.</h2><p>Tell us where you are today. We’ll come back with the right next step—not a generic agency deck.</p><div className="contact-note"><CircleCheck size={18}/> No pressure. Just a useful first diagnosis.</div></div><form className="contact-form" onSubmit={submit}>{sent ? <div className="success"><CircleCheck size={34}/><h3>Brief received.</h3><p>Thanks — the CartMakers team will review it and get back to you.</p></div> : <><label>Name<input name="name" required placeholder="Your name" /></label><label>Email<input name="email" type="email" required placeholder="you@company.com" /></label><label>Company<input name="company" placeholder="Brand or company" /></label><label>What should we look at first?<textarea name="message" required placeholder="Store, checkout, tracking, COD..." rows="4" /></label>{error && <p className="form-error">{error}</p>}<button className="button primary submit" disabled={busy}>{busy ? 'Sending...' : 'Send the brief'} <ArrowUpRight size={18}/></button></>}</form></section>
    </main>
    <footer className="footer shell"><div className="brand footer-brand"><img src="/assets/cartmakers-symbol.svg"/><span>Cart<span>Makers</span></span></div><span>Ecommerce Systems & Growth</span><span>© 2026 CartMakers</span></footer>
  </>;
}
createRoot(document.getElementById('root')).render(<App />);

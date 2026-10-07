import Link from "next/link";

export default function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <header className="topbar">
        <Link href="/" className="brand">
          <span className="brand-mark" aria-hidden>
            ∀
          </span>
          Révisions
        </Link>
      </header>
      {children}
    </>
  );
}

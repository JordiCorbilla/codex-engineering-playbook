import type { ReactNode } from "react";

type StatusPanelProps = {
  title: string;
  children: ReactNode;
};

export function StatusPanel({ title, children }: StatusPanelProps) {
  return (
    <section className="status-panel" aria-labelledby="status-panel-title">
      <header className="status-panel__header">
        <div>
          <p className="section-label">Review queue</p>
          <h2 id="status-panel-title">{title}</h2>
        </div>
        <span className="status-chip">Live demo state</span>
      </header>
      <div className="status-panel__body">{children}</div>
    </section>
  );
}

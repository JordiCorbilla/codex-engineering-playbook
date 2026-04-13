import "./DataPanel.css";

type DataPanelProps = {
  title: string;
  description?: string;
  children: React.ReactNode;
};

export function DataPanel({ title, description, children }: DataPanelProps) {
  return (
    <section className="data-panel" aria-labelledby="data-panel-title">
      <header className="data-panel__header">
        <h2 id="data-panel-title">{title}</h2>
        {description ? <p>{description}</p> : null}
      </header>
      <div className="data-panel__body">{children}</div>
    </section>
  );
}

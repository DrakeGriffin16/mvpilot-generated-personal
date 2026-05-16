-- Suggested Postgres schema for personal-portfolio
create table if not exists personal_portfolio_intakes (
  id uuid primary key default gen_random_uuid(),
  user_goal text not null,
  urgency text not null default 'normal',
  notes text,
  status text not null default 'new',
  created_at timestamptz not null default now()
);

create index if not exists personal_portfolio_intakes_status_idx
  on personal_portfolio_intakes(status, created_at desc);
# Data Dictionary

The project uses fictional, reproducible sample data. The fields are designed to resemble Commercial IT, Sales Consulting and building-service reporting scenarios.

## customers.csv

| Field | Meaning |
| --- | --- |
| `customer_id` | Stable customer identifier |
| `name` | Fictional customer name |
| `industry` | Customer industry |
| `region` | Broad sales/service region |
| `security_systems` | Approximate number of security/building technology systems |
| `annual_revenue_eur` | Estimated annual revenue potential in EUR |
| `strategic_priority` | Internal account priority from 1 to 5 |

## projects.csv

| Field | Meaning |
| --- | --- |
| `project_id` | Stable project identifier |
| `customer_id` | Related customer |
| `project_name` | Project opportunity name |
| `category` | Commercial IT, ERP & Data, Process Digitization, Sales Enablement or Sales & Consulting |
| `phase` | Pipeline phase: idea, workshop, proposal or delivery |
| `estimated_value_eur` | Estimated project value in EUR |
| `estimated_cost_eur` | Estimated delivery cost in EUR |
| `manual_hours_per_month` | Current monthly manual effort |
| `automated_hours_per_month` | Expected monthly effort after improvement |
| `implementation_weeks` | Estimated implementation time |
| `consulting_fit` | Consulting fit from 1 to 5 |
| `delivery_risk` | Delivery risk from 1 to 5 |

## service_metrics.csv

| Field | Meaning |
| --- | --- |
| `metric_id` | Stable metric row identifier |
| `customer_id` | Related customer |
| `month` | Reporting month |
| `service_tickets` | Number of service tickets |
| `sla_breaches` | Number of SLA breaches |
| `average_resolution_hours` | Average ticket resolution time |
| `system_downtime_hours` | Monthly system downtime |

## workshops.csv

| Field | Meaning |
| --- | --- |
| `workshop_id` | Stable workshop identifier |
| `project_id` | Related project |
| `stakeholders` | Number of workshop stakeholders |
| `requirements_clarity` | Requirements clarity from 1 to 5 |
| `customer_readiness` | Customer readiness from 1 to 5 |
| `technical_complexity` | Technical complexity from 1 to 5 |
| `commercial_urgency` | Commercial urgency from 1 to 5 |


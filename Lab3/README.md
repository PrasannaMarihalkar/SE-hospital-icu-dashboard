# Lab 3 - Component Modelling & Architectural Pattern Selection

**Student:** Prasanna Chidambar Marihalkar
**SRN:** PES1UG24CS684
**System:** Hospital Bed & ICU Allocation Dashboard
**Selected architecture:** Client-Server

## Files

| File | What it is |
|------|------------|
| `Component_Diagram.png` / `Component_Diagram.pdf` | UML component diagram (6 components, 7 interfaces) |
| `Architecture_Justification.docx` / `Architecture_Justification.pdf` | One-page written justification |

## Components

| Tier | Component |
|------|-----------|
| Client | Dashboard UI |
| Server | Auth & Audit Service, Bed Allocation Manager, Bed Availability Service, Bed Status Manager, Hospital Bed Database |

## Interfaces

| ID | Interface | Provided by | Required by | Protocol |
|----|-----------|-------------|-------------|----------|
| I1 | IAuthentication | Auth & Audit Service | Dashboard UI | HTTPS/TLS, JWT |
| I2 | IAllocationAPI | Bed Allocation Manager | Dashboard UI | REST over HTTPS |
| I3 | IAccessCheck | Auth & Audit Service | Bed Allocation Manager | Internal REST |
| I4 | IAvailabilityCheck | Bed Availability Service | Bed Allocation Manager | Internal API |
| I5 | IStatusUpdate | Bed Status Manager | Bed Allocation Manager | Internal API |
| I6 | IBedData | Hospital Bed Database | Bed Availability Service | SQL/JDBC (read) |
| I7 | IStatusData | Hospital Bed Database | Bed Status Manager | SQL/JDBC (write) |

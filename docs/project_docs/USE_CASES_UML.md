# Use Case Diagrams

## Main System Use Cases

Use https://github.com/mermaid-js/mermaid/pull/6141

```mermaid
usecase-beta
    title Data Visualization Platform Use Cases

    actor User
    service XLSXFiles
    service EmailSystem

    systemboundary
        title Data Visualization Platform
        (Manage Quarters)
        (Upload XLSX Files)
        (Delete XLSX Files)
        (View Data Visualizations)
        (Apply Advanced Filters)
        (Manage Account)
    end

    User -> (Manage Quarters)
    User -> (Upload XLSX Files) -> XLSXFiles
    User -> (Delete XLSX Files) -> XLSXFiles
    User -> (View Data Visualizations)
    User -> (Apply Advanced Filters)
    User -> (Manage Account)
```

## Account Management Use Cases

```mermaid
usecase-beta
    title Account Management Use Cases

    actor User
    service EmailSystem

    systemboundary
        title Authentication System
        (Login)
        (Create Account)
        (Change Password)
        (Recover Password)
    end

    User -> (Login)
    User -> (Create Account)
    User -> (Change Password)
    User -> (Recover Password) -> EmailSystem
```

## Data Management Use Cases

```mermaid
usecase-beta
    title Data Management Use Cases

    actor User
    service XLSXFiles

    systemboundary
        title Data Management System
        (Create Quarter)
        (Upload XLSX)
        (Delete XLSX)
        (View Charts)
        (Apply Filters)
    end

    User -> (Create Quarter)
    User -> (Upload XLSX) -> XLSXFiles
    User -> (Delete XLSX) -> XLSXFiles
    User -> (View Charts)
    User -> (Apply Filters)
```

## System Context

```mermaid
usecase-beta
    title System Context

    actor User
    service XLSXFiles
    service EmailSystem

    systemboundary
        title Data Visualization Platform
        (Process XLSX Data)
        (Send Email Notifications)
    end

    User -> (Process XLSX Data) -> XLSXFiles
    (Send Email Notifications) -> EmailSystem
``` 
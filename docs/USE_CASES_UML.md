# Use Case Diagrams

## Main System Use Cases

Use https://github.com/mermaid-js/mermaid/pull/6141

```mermaid
usecase-beta
    title Data Visualization Platform Use Cases

    actor GroupUser
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

    GroupUser -> (Manage Quarters)
    GroupUser -> (Upload XLSX Files) -> XLSXFiles
    GroupUser -> (Delete XLSX Files) -> XLSXFiles
    GroupUser -> (View Data Visualizations)
    GroupUser -> (Apply Advanced Filters)
    GroupUser -> (Manage Account)
```

## Account Management Use Cases

```mermaid
usecase-beta
    title Account Management Use Cases

    actor GroupUser
    service EmailSystem

    systemboundary
        title Authentication System
        (Login)
        (Create Account)
        (Change Password)
        (Recover Password)
    end

    GroupUser -> (Login)
    GroupUser -> (Create Account)
    GroupUser -> (Change Password)
    GroupUser -> (Recover Password) -> EmailSystem
```

## Data Management Use Cases

```mermaid
usecase-beta
    title Data Management Use Cases

    actor GroupUser
    service XLSXFiles

    systemboundary
        title Data Management System
        (Create Quarter)
        (Upload XLSX)
        (Delete XLSX)
        (View Charts)
        (Apply Filters)
    end

    GroupUser -> (Create Quarter)
    GroupUser -> (Upload XLSX) -> XLSXFiles
    GroupUser -> (Delete XLSX) -> XLSXFiles
    GroupUser -> (View Charts)
    GroupUser -> (Apply Filters)
```

## System Context

```mermaid
usecase-beta
    title System Context

    actor GroupUser
    service XLSXFiles
    service EmailSystem

    systemboundary
        title Data Visualization Platform
        (Process XLSX Data)
        (Send Email Notifications)
    end

    GroupUser -> (Process XLSX Data) -> XLSXFiles
    (Send Email Notifications) -> EmailSystem
``` 
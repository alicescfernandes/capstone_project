# Project Requirements

## Functional Requirements (FR)

### FR01. User Authentication
- The system must allow a user to create an account.
- The system must allow a user to log in using email and password.
- The system must allow users to recover their password via email.
- The system must allow users to change their password after logging in.

### FR02. File Management
- The system must allow users to upload `.xlsx` files.
- The system must associate uploaded files with specific quarters (e.g., "Quarter 1").
- The system must allow users to delete previously uploaded files.

### FR03. Quarter Management
- The system must allow users to create quarters identified by "Quarter N".
- The system must list all quarters created by the User.

### FR04. Data Visualization
- The system must display charts based on the uploaded `.xlsx` files.
- The system must support advanced filtering on the charts.

### FR05. User Isolation
- Each User must only have access to its own data and quarters.
- Data must be compartmentalized per User to ensure privacy.

---

## Non-Functional Requirements (NFR)

### NFR01. Usability
- The interface must be intuitive and easy to navigate for students with basic computer skills.
- The UI must follow the Flowbite design system for visual consistency.

### NFR02. Security
- Authentication must follow Django’s default authentication system.
- The system must ensure that users can only access their own data.
- Passwords must be securely stored using hashing.

### NFR03. Performance
- Chart loading time should be under 3 seconds for average-sized files.
- The application must support multiple concurrent users without significant performance degradation.

### NFR04. Reliability
- The system must ensure persistence of uploaded files and prevent data loss.
- Filters applied to charts must always produce accurate and consistent results.

### NFR05. Compatibility
- The application must be compatible with major browsers (Chrome, Firefox, Edge).
- The application must support `.xlsx` files exported from the Marketplace Simulations platform without needing manual formatting.

### NFR06. Maintainability
- The system must be built using the Django framework to ensure scalability and maintainability.
- The codebase must follow best practices to allow for collaboration between developers.

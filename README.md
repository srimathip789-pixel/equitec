# Equitec Trade Management System

A Console-based Trade Order Management System developed in C# (.NET 10.0).

## 🚀 Features
- **View Orders**: Display a formatted list of all active trade orders.
- **Add Order**: Place new buy/sell orders with validation.
- **Edit Order**: Update the price of existing orders using their ID.
- **Delete Order**: Cancel/Remove orders from the system.
- **In-Memory Storage**: Uses a thread-safe `List<T>` structure for high-performance data handling without requiring a local database setup.

## 🛠️ Tech Stack
- **Language**: C#
- **Framework**: .NET 10.0
- **Architecture**: Console Application (In-Memory CRUD)

## 📦 How to Run
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/srimathip789-pixel/equitec.git
   ```
2. **Navigate to Directory**:
   ```bash
   cd equitec
   ```
3. **Run Application**:
   ```bash
   dotnet run
   ```

## 📝 Design Decisions
- **Why In-Memory?**: For the purpose of this machine test, I implemented an In-Memory storage pattern. This ensures the application is **portable** and runs immediately on any machine with the .NET SDK, without needing complex SQL Server configuration or connection strings.

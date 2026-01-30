using System;
using System.Collections.Generic;
using System.Linq;

namespace EquitecMachineTest
{
    // === Data Model ===
    public class TradeOrder
    {
        public int OrderId { get; set; }
        public string ClientName { get; set; }
        public string StockSymbol { get; set; }
        public int Quantity { get; set; }
        public decimal Price { get; set; }
        public string OrderType { get; set; } // BUY or SELL
    }

    class Program
    {
        // === IN-MEMORY STORAGE (Replaces Database) ===
        static List<TradeOrder> tradeOrders = new List<TradeOrder>();
        static int nextId = 1;

        static void Main(string[] args)
        {
            Console.Title = "Equitec Machine Test - Trade Orders (In-Memory)";
            
            // Add some dummy data to start with
            tradeOrders.Add(new TradeOrder { OrderId = nextId++, ClientName = "Demo Client", StockSymbol = "EQU.IT", Quantity = 100, Price = 150.50m, OrderType = "BUY" });

            while (true)
            {
                Console.Clear();
                Console.ForegroundColor = ConsoleColor.Cyan;
                Console.WriteLine("=========================================");
                Console.WriteLine("    EQUITEC TRADE MANAGEMENT SYSTEM      ");
                Console.WriteLine("    (Running in In-Memory Mode)          ");
                Console.WriteLine("=========================================");
                Console.ResetColor();
                Console.WriteLine("1. [VIEW]   All Trade Orders");
                Console.WriteLine("2. [ADD]    Place New Order");
                Console.WriteLine("3. [EDIT]   Update Order Price");
                Console.WriteLine("4. [DELETE] Cancel Order");
                Console.WriteLine("5. [EXIT]   Close Application");
                Console.WriteLine("-----------------------------------------");
                Console.Write("Select an Option (1-5): ");
                
                string choice = Console.ReadLine();

                try 
                {
                    switch (choice)
                    {
                        case "1": ReadOrders(); break;
                        case "2": CreateOrder(); break;
                        case "3": UpdateOrder(); break;
                        case "4": DeleteOrder(); break;
                        case "5": return;
                        default: 
                            PrintMessage("Invalid choice! Press Enter.", ConsoleColor.Red);
                            break;
                    }
                }
                catch (Exception ex)
                {
                    PrintMessage($"\n[CRITICAL ERROR]: {ex.Message}", ConsoleColor.Red);
                }

                Console.WriteLine("\nPress any key to return to menu...");
                Console.ReadKey();
            }
        }

        // --- 1. READ (View All) ---
        static void ReadOrders()
        {
            Console.WriteLine("\n--- Fetching Orders... ---");
            
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("\nID | Client         | Stock      | Qty | Price       | Type");
            Console.WriteLine("------------------------------------------------------------");
            Console.ResetColor();

            if (tradeOrders.Count == 0)
            {
                Console.WriteLine("(No orders found)");
            }
            else
            {
                foreach (var order in tradeOrders)
                {
                    Console.WriteLine($"{order.OrderId,-2} | {order.ClientName,-14} | {order.StockSymbol,-10} | {order.Quantity,-3} | {order.Price,-11:C2} | {order.OrderType}");
                }
            }
        }

        // --- 2. CREATE (Insert) ---
        static void CreateOrder()
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("\n--- Place New Trade Order ---");
            Console.ResetColor();

            string client = GetValidString("Client Name: ");
            string symbol = GetValidString("Stock Symbol (e.g. TCS): ");
            int qty = GetValidInt("Quantity: ");
            decimal price = GetValidDecimal("Price: ");
            
            Console.Write("Type (BUY/SELL): ");
            string type = Console.ReadLine()?.ToUpper();
            if (string.IsNullOrWhiteSpace(type)) type = "BUY"; // Default

            // Add to List
            var newOrder = new TradeOrder
            {
                OrderId = nextId++,
                ClientName = client,
                StockSymbol = symbol,
                Quantity = qty,
                Price = price,
                OrderType = type
            };
            tradeOrders.Add(newOrder);

            PrintMessage(">>> Success! Order successfully placed in Memory.", ConsoleColor.Green);
        }

        // --- 3. UPDATE ---
        static void UpdateOrder()
        {
            Console.WriteLine("\n--- Update Order Price ---");
            ReadOrders(); // Show list first so they know ID
            
            int id = GetValidInt("\nEnter Order ID to Update: ");

            var order = tradeOrders.FirstOrDefault(o => o.OrderId == id);
            if (order == null)
            {
                PrintMessage(">>> Error: Order ID not found.", ConsoleColor.Red);
                return;
            }

            decimal price = GetValidDecimal("Enter New Price: ");

            // Update Object
            order.Price = price;
            PrintMessage(">>> Price updated successfully!", ConsoleColor.Green);
        }

        // --- 4. DELETE ---
        static void DeleteOrder()
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("\n--- Cancel (Delete) Order ---");
            Console.ResetColor();
            ReadOrders();

            int id = GetValidInt("\nEnter Order ID to Delete: ");

            var order = tradeOrders.FirstOrDefault(o => o.OrderId == id);
            if (order == null)
            {
                PrintMessage(">>> Error: Order ID not found.", ConsoleColor.Red);
                return;
            }

            // Remove from List
            tradeOrders.Remove(order);
            PrintMessage(">>> Order cancelled (Deleted)!", ConsoleColor.Yellow);
        }

        // === HELPER METHODS ===

        static string GetValidString(string prompt)
        {
            string input;
            do
            {
                Console.Write(prompt);
                input = Console.ReadLine();
                if (string.IsNullOrWhiteSpace(input))
                {
                    PrintMessage("Input cannot be empty. Please try again.", ConsoleColor.DarkYellow);
                }
            } while (string.IsNullOrWhiteSpace(input));
            return input;
        }

        static int GetValidInt(string prompt)
        {
            int value;
            while (true)
            {
                Console.Write(prompt);
                if (int.TryParse(Console.ReadLine(), out value) && value > 0)
                {
                    return value;
                }
                PrintMessage("Invalid number. Please enter a valid positive integer.", ConsoleColor.DarkYellow);
            }
        }

        static decimal GetValidDecimal(string prompt)
        {
            decimal value;
            while (true)
            {
                Console.Write(prompt);
                if (decimal.TryParse(Console.ReadLine(), out value) && value > 0)
                {
                    return value;
                }
                PrintMessage("Invalid price. Please enter a valid positive decimal.", ConsoleColor.DarkYellow);
            }
        }

        static void PrintMessage(string message, ConsoleColor color)
        {
            Console.ForegroundColor = color;
            Console.WriteLine(message);
            Console.ResetColor();
        }
    }
}

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
                            Console.ForegroundColor = ConsoleColor.Red;
                            Console.WriteLine("Invalid choice! Press Enter.");
                            Console.ResetColor();
                            break;
                    }
                }
                catch (Exception ex)
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine($"\n[CRITICAL ERROR]: {ex.Message}");
                    Console.ResetColor();
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
            Console.WriteLine("\nID | Client         | Stock      | Qty | Price     | Type");
            Console.WriteLine("----------------------------------------------------------");
            Console.ResetColor();

            if (tradeOrders.Count == 0)
            {
                Console.WriteLine("(No orders found)");
            }
            else
            {
                foreach (var order in tradeOrders)
                {
                    Console.WriteLine($"{order.OrderId,-2} | {order.ClientName,-14} | {order.StockSymbol,-10} | {order.Quantity,-3} | {order.Price,-9} | {order.OrderType}");
                }
            }
        }

        // --- 2. CREATE (Insert) ---
        static void CreateOrder()
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("\n--- Place New Trade Order ---");
            Console.ResetColor();

            Console.Write("Client Name: ");
            string client = Console.ReadLine();
            
            Console.Write("Stock Symbol (e.g. TCS): ");
            string symbol = Console.ReadLine();
            
            Console.Write("Quantity: ");
            if (!int.TryParse(Console.ReadLine(), out int qty)) { Console.WriteLine("Invalid Quantity!"); return; }
            
            Console.Write("Price: ");
            if (!decimal.TryParse(Console.ReadLine(), out decimal price)) { Console.WriteLine("Invalid Price!"); return; }
            
            Console.Write("Type (BUY/SELL): ");
            string type = Console.ReadLine().ToUpper();

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

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine(">>> Success! Order successfully placed in Memory.");
            Console.ResetColor();
        }

        // --- 3. UPDATE ---
        static void UpdateOrder()
        {
            Console.WriteLine("\n--- Update Order Price ---");
            ReadOrders(); // Show list first so they know ID
            
            Console.Write("\nEnter Order ID to Update: ");
            if (!int.TryParse(Console.ReadLine(), out int id)) return;

            var order = tradeOrders.FirstOrDefault(o => o.OrderId == id);
            if (order == null)
            {
                Console.WriteLine(">>> Error: Order ID not found.");
                return;
            }

            Console.Write("Enter New Price: ");
            if (!decimal.TryParse(Console.ReadLine(), out decimal price)) return;

            // Update Object
            order.Price = price;
            Console.WriteLine(">>> Price updated successfully!");
        }

        // --- 4. DELETE ---
        static void DeleteOrder()
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("\n--- Cancel (Delete) Order ---");
            Console.ResetColor();
            ReadOrders();

            Console.Write("\nEnter Order ID to Delete: ");
            if (!int.TryParse(Console.ReadLine(), out int id)) return;

            var order = tradeOrders.FirstOrDefault(o => o.OrderId == id);
            if (order == null)
            {
                Console.WriteLine(">>> Error: Order ID not found.");
                return;
            }

            // Remove from List
            tradeOrders.Remove(order);
            Console.WriteLine(">>> Order cancelled (Deleted)!");
        }
    }
}

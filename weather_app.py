# Import required libraries
# tkinter is Python's standard GUI library
import tkinter as tk
from tkinter import ttk, messagebox  # ttk provides themed widgets, messagebox for popup messages
import requests  # For making HTTP requests to the weather API
import os
from dotenv import load_dotenv  # For loading environment variables (not used in current version)

print("Starting Weather App...")

# API key for OpenWeatherMap service
# This key is used to authenticate our requests to the weather API
api_key = "bc11bf7e559b891384cc94b824bd1eb1"
print(f"Using API key: {api_key}")

class WeatherApp:
    """
    Main application class that handles the GUI and weather data fetching
    """
    def __init__(self, root):
        """
        Initialize the application window and all its components
        :param root: The main window of the application
        """
        print("Initializing Weather App GUI...")
        # Configure the main window
        self.root = root
        self.root.title("Weather App")  # Set window title
        self.root.geometry("400x500")   # Set window size
        self.root.configure(bg="#f0f0f0")  # Set background color
        
        # Configure the visual styles for the widgets
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")  # Style for frames
        style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))  # Style for labels
        style.configure("TButton", font=("Helvetica", 12))  # Style for buttons
        style.configure("TEntry", font=("Helvetica", 12))   # Style for text entries
        
        # Create the main container frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)  # Make frame expand to fill window
        
        # Create and configure the title label
        self.title_label = ttk.Label(
            self.main_frame,
            text="Weather Forecast",
            font=("Helvetica", 24, "bold")
        )
        self.title_label.pack(pady=20)  # Add vertical padding
        
        # Create frame for city input and search button
        self.city_frame = ttk.Frame(self.main_frame)
        self.city_frame.pack(fill=tk.X, pady=20)  # Make frame expand horizontally
        
        # Create the city input field
        self.city_entry = ttk.Entry(self.city_frame, width=30)
        self.city_entry.pack(side=tk.LEFT, padx=5)
        self.city_entry.insert(0, "Enter city name...")  # Default placeholder text
        # Bind the FocusIn event to clear placeholder text when clicked
        self.city_entry.bind("<FocusIn>", self.clear_placeholder)
        
        # Create the search button
        self.search_button = ttk.Button(
            self.city_frame,
            text="Search",
            command=self.get_weather  # Link button to get_weather method
        )
        self.search_button.pack(side=tk.LEFT, padx=5)
        
        # Create frame for weather information display
        self.weather_frame = ttk.Frame(self.main_frame)
        self.weather_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create labels for displaying weather information
        # Temperature label (large font for emphasis)
        self.temp_label = ttk.Label(
            self.weather_frame,
            text="",
            font=("Helvetica", 36)
        )
        self.temp_label.pack(pady=20)
        
        # Weather description label
        self.desc_label = ttk.Label(
            self.weather_frame,
            text="",
            font=("Helvetica", 14)
        )
        self.desc_label.pack()
        
        # Additional weather details label
        self.details_label = ttk.Label(
            self.weather_frame,
            text="",
            font=("Helvetica", 12)
        )
        self.details_label.pack(pady=10)
        
        # Store API key for later use
        self.api_key = api_key
        print("GUI initialization complete!")
    
    def clear_placeholder(self, event):
        """
        Clear the placeholder text when user clicks the input field
        :param event: The event object (not used but required for event binding)
        """
        if self.city_entry.get() == "Enter city name...":
            self.city_entry.delete(0, tk.END)
    
    def get_weather(self):
        """
        Fetch and display weather data for the entered city
        This method is called when the search button is clicked
        """
        # Get the city name from the input field
        city = self.city_entry.get()
        if city == "" or city == "Enter city name...":
            messagebox.showwarning("Input Error", "Please enter a city name!")
            return
        
        try:
            print(f"Fetching weather data for {city}...")
            # Construct the API URL with the city name and API key
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            # Make the API request
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                # Successfully got weather data
                # Extract relevant information from the response
                temp = data["main"]["temp"]  # Current temperature
                desc = data["weather"][0]["description"].capitalize()  # Weather description
                feels_like = data["main"]["feels_like"]  # "Feels like" temperature
                humidity = data["main"]["humidity"]  # Humidity percentage
                wind_speed = data["wind"]["speed"]  # Wind speed
                
                # Update the GUI labels with weather information
                self.temp_label.config(text=f"{temp:.1f}°C")
                self.desc_label.config(text=desc)
                self.details_label.config(
                    text=f"Feels like: {feels_like:.1f}°C\n"
                         f"Humidity: {humidity}%\n"
                         f"Wind Speed: {wind_speed} m/s"
                )
                print("Weather data updated successfully!")
            else:
                # Handle API error response
                print(f"Error: {data.get('message', 'Unknown error')}")
                messagebox.showerror(
                    "Error",
                    f"Error getting weather data: {data.get('message', 'Unknown error')}"
                )
                
        except requests.RequestException as e:
            # Handle network-related errors
            print(f"Network error: {str(e)}")
            messagebox.showerror("Error", f"Network error: {str(e)}")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"Unexpected error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# This is the entry point of the program
if __name__ == "__main__":
    print("Creating main window...")
    root = tk.Tk()  # Create the main window
    app = WeatherApp(root)  # Create our application instance
    print("Starting main loop...")
    root.mainloop()  # Start the GUI event loop
    print("Application closed.") 
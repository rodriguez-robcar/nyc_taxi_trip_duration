import matplotlib.pyplot as plt
import seaborn as sns

def plot_vendor_distribution(df):
    
    df["vendor_id"].value_counts().sort_values().plot(kind='bar')
    
    plt.title("Vendor ID Distribution")
    plt.xlabel("Vendor ID")
    plt.ylabel("Count")
    plt.show()

def plot_trip_duration_distribution(df):
    
    fig, (ax_box, ax_hist) = plt.subplots(2, figsize=(12, 12))

    # Using log of trip_duration because it's usually heavily skewed
    sns.boxplot(x='vendor_id', y='trip_duration', data=df, ax=ax_box)

    ax_box.set_xlabel('Vendor ID')
    ax_box.set_ylabel('Trip Duration in seconds (log scale)')
    ax_box.set_title('Box Plot of Trip Duration by Vendor ID')
    ax_box.set_yscale('log') # Use log scale to handle outliers

    # Using log of trip_duration for KDE plot as well
    sns.kdeplot(data=df, 
                x='trip_duration', 
                hue='vendor_id', 
                log_scale=True, 
                ax=ax_hist)

    ax_hist.set_xlabel('Trip Duration in seconds (log scale)')
    ax_hist.set_ylabel('Density')
    ax_hist.set_title('Kernel Density Plot of Trip Duration by Vendor ID')

    plt.tight_layout()
    plt.show()

def plot_passenger_count_distribution(df):
    
    # Assuming your data is in a DataFrame 'df'
    plt.figure(figsize=(10, 6))

    plt.hist(df[df['vendor_id'] == 1]['passenger_count'], 
         bins=10, alpha=0.5, label='Vendor 1', color='blue')

    plt.hist(df[df['vendor_id'] == 2]['passenger_count'], 
         bins=10, alpha=0.5, label='Vendor 2', color='red')

    plt.xlabel('Passenger Count')
    plt.ylabel('Trip Frequency')
    plt.title('Passenger Count Distribution by Vendor')
    plt.xticks(range(0, 11))
    plt.legend()
    plt.show()

def plot_pickup_time_distribution(df):
    
    # Visualize the distribution of pickup month, day, and hour
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    months = ["January", "February", "March", "April", "May", "June"]

    axes[0].hist(df["pickup_month"], bins=6, color='skyblue', edgecolor='black')
    axes[0].set_title("Pickup Month Distribution")
    axes[0].set_xlabel("Month")
    axes[0].set_xticks(range(1, 7))
    axes[0].set_xticklabels(months, rotation=45)
    axes[0].set_ylabel("Frequency")

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    axes[1].hist(df["pickup_day"], bins=7, color='lightgreen', edgecolor='black')
    axes[1].set_title("Pickup Day Distribution")
    axes[1].set_xlabel("Day of Month")
    axes[1].set_xticks(range(7))
    axes[1].set_xticklabels(days, rotation=45)
    axes[1].set_ylabel("Frequency")

    axes[2].hist(df["pickup_hour"], bins=24, color='lightcoral', edgecolor='black')
    axes[2].set_title("Pickup Hour Distribution")
    axes[2].set_xlabel("Hour of Day")
    axes[2].set_ylabel("Frequency")

    plt.tight_layout()
    plt.show()
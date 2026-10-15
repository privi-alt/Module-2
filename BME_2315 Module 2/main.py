# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Get the folder where main.py is located
base_folder = Path(__file__).resolve().parent

# Load the main FSHD dataset
df = pd.read_csv(base_folder / "Module2_FSHD_Dataset.csv")

# Check that the dataset loaded correctly
print("Main FSHD dataset shape:")
print(df.shape)

print("\nFirst five rows:")
print(df.head())

# Path to the MRI data
mri_folder = (
    base_folder
    / "FSHD_MRI_data"
    / "FSHD_MRI_data"
    / "FSHD_TA_MRI_data_0020_TP1_TP2"
)

# Load the MRI slice information
slice_info = pd.read_csv(mri_folder / "slice_info.csv")

print("\nMRI slice information:")
print(slice_info.head())

print("\nMRI dataset shape:")
print(slice_info.shape)

print("\nMRI columns:")
print(slice_info.columns)

# Select the first MRI slice as an example
first_slice = slice_info.iloc[0]

# Find the matching water, fat, and mask files
water_path = mri_folder / first_slice["water_file"]
fat_path = mri_folder / first_slice["fat_file"]
mask_path = mri_folder / first_slice["mask_file"]

# Load the MRI images and TA mask
water_image = np.load(water_path)
fat_image = np.load(fat_path)
ta_mask = np.load(mask_path)

print("\nLoaded MRI slice:")
print("Subject:", first_slice["subject"])
print("Timepoint:", first_slice["timepoint"])
print("Slice ID:", first_slice["slice_id"])

# Check the dimensions of the arrays
print("\nArray dimensions:")
print("Water image shape:", water_image.shape)
print("Fat image shape:", fat_image.shape)
print("TA mask shape:", ta_mask.shape)

if water_image.shape == fat_image.shape == ta_mask.shape:
    print("All three arrays have matching dimensions.")
else:
    print("WARNING: The array dimensions do not match.")

# Check that the TA mask is binary
print("\nUnique values in the TA mask:")
print(np.unique(ta_mask))

# Show the water MRI
plt.figure()
plt.imshow(water_image, cmap="gray")
plt.title("TP1 Slice 1 - Water MRI")
plt.xlabel("Pixel column")
plt.ylabel("Pixel row")
plt.tight_layout()
plt.savefig(base_folder / "tp1_slice1_water.png", dpi=300)
plt.show()

# Show the fat MRI
plt.figure()
plt.imshow(fat_image, cmap="gray")
plt.title("TP1 Slice 1 - Fat MRI")
plt.xlabel("Pixel column")
plt.ylabel("Pixel row")
plt.tight_layout()
plt.savefig(base_folder / "tp1_slice1_fat.png", dpi=300)
plt.show()

# Show the tibialis anterior mask
plt.figure()
plt.imshow(ta_mask, cmap="gray")
plt.title("TP1 Slice 1 - Tibialis Anterior Mask")
plt.xlabel("Pixel column")
plt.ylabel("Pixel row")
plt.tight_layout()
plt.savefig(base_folder / "tp1_slice1_ta_mask.png", dpi=300)
plt.show()

# Overlay the TA mask on the water MRI
plt.figure()
plt.imshow(water_image, cmap="gray")
plt.contour(ta_mask, levels=[0.5])
plt.title("TP1 Slice 1 - Water MRI with TA Mask")
plt.xlabel("Pixel column")
plt.ylabel("Pixel row")
plt.tight_layout()
plt.savefig(base_folder / "tp1_slice1_water_with_mask.png", dpi=300)
plt.show()

# Overlay the TA mask on the fat MRI
plt.figure()
plt.imshow(fat_image, cmap="gray")
plt.contour(ta_mask, levels=[0.5])
plt.title("TP1 Slice 1 - Fat MRI with TA Mask")
plt.xlabel("Pixel column")
plt.ylabel("Pixel row")
plt.tight_layout()
plt.savefig(base_folder / "tp1_slice1_fat_with_mask.png", dpi=300)
plt.show()

# Calculate fat fraction for the example slice
total_signal = water_image + fat_image

# Only use pixels where there is MRI signal
valid_pixels = total_signal > 0

# Create the fat fraction image
fat_fraction = np.zeros_like(fat_image, dtype=float)

# Fat Fraction = Fat / (Water + Fat) x 100
fat_fraction[valid_pixels] = (
    fat_image[valid_pixels] / total_signal[valid_pixels]
) * 100

# Select valid pixels inside the tibialis anterior
ta_region = (ta_mask == 1) & valid_pixels
ta_fat_fraction = fat_fraction[ta_region]

# Whole-image statistics
whole_image_values = fat_fraction[valid_pixels]

whole_image_mean = np.mean(whole_image_values)
whole_image_median = np.median(whole_image_values)
whole_image_std = np.std(whole_image_values)
whole_image_pixel_count = len(whole_image_values)

# TA statistics
ta_mean = np.mean(ta_fat_fraction)
ta_median = np.median(ta_fat_fraction)
ta_std = np.std(ta_fat_fraction)
ta_pixel_count = len(ta_fat_fraction)

print("\nFat Fraction Summary for TP1 Slice 1:")
print("Whole-image mean:", whole_image_mean, "%")
print("Whole-image median:", whole_image_median, "%")
print("Whole-image standard deviation:", whole_image_std, "%")
print("Whole-image valid pixels:", whole_image_pixel_count)

print("\nTA mean fat fraction:", ta_mean, "%")
print("TA median fat fraction:", ta_median, "%")
print("TA standard deviation:", ta_std, "%")
print("Number of TA pixels:", ta_pixel_count)

# Show the fat fraction map
plt.figure()
plt.imshow(fat_fraction, vmin=0, vmax=100)
plt.colorbar(label="Fat Fraction (%)")
plt.contour(ta_mask, levels=[0.5])
plt.title("TP1 Slice 1 - Fat Fraction Map with TA Boundary")
plt.xlabel("Pixel column")
plt.ylabel("Pixel row")
plt.tight_layout()
plt.savefig(base_folder / "tp1_slice1_fat_fraction_map.png", dpi=300)
plt.show()

# Show the distribution of fat fraction inside the TA
plt.figure()
plt.hist(ta_fat_fraction, bins=20)
plt.title("TP1 Slice 1 - TA Fat Fraction Distribution")
plt.xlabel("Fat Fraction (%)")
plt.ylabel("Number of Pixels")
plt.tight_layout()
plt.savefig(base_folder / "tp1_slice1_ta_fat_fraction_histogram.png", dpi=300)
plt.show()

# Analyze all 16 MRI slices
results = []

for _, row in slice_info.iterrows():

    # Load the water, fat, and mask files for this slice
    water = np.load(mri_folder / row["water_file"])
    fat = np.load(mri_folder / row["fat_file"])
    mask = np.load(mri_folder / row["mask_file"])

    # Make sure the arrays match
    if not (water.shape == fat.shape == mask.shape):
        print("Skipping slice because dimensions do not match:", row["slice_id"])
        continue

    # Calculate fat fraction
    total_signal = water + fat
    valid_pixels = total_signal > 0

    slice_fat_fraction = np.zeros_like(fat, dtype=float)

    slice_fat_fraction[valid_pixels] = (
        fat[valid_pixels] / total_signal[valid_pixels]
    ) * 100

    # Select valid pixels inside the TA
    ta_region = (mask == 1) & valid_pixels
    ta_values = slice_fat_fraction[ta_region]

    # Get the valid whole-image values
    whole_values = slice_fat_fraction[valid_pixels]

    # Save the results from this slice
    results.append({
        "subject": row["subject"],
        "timepoint": row["timepoint"],
        "slice_id": row["slice_id"],
        "percent_along_muscle": row["percent_along_muscle"],
        "distance_from_muscle_start_mm": row["distance_from_muscle_start_mm"],
        "whole_image_mean_ff": np.mean(whole_values),
        "whole_image_median_ff": np.median(whole_values),
        "whole_image_std_ff": np.std(whole_values),
        "whole_image_pixel_count": len(whole_values),
        "ta_mean_ff": np.mean(ta_values),
        "ta_median_ff": np.median(ta_values),
        "ta_std_ff": np.std(ta_values),
        "ta_pixel_count": len(ta_values)
    })

# Turn the results into a DataFrame
results_df = pd.DataFrame(results)

print("\nMRI Fat Fraction Results:")
print(results_df)

# Save all slice results
results_df.to_csv(
    base_folder / "mri_fat_fraction_results.csv",
    index=False
)

print("\nMRI results saved to mri_fat_fraction_results.csv")

# Summarize TA fat fraction at TP1 and TP2
timepoint_summary = results_df.groupby("timepoint")["ta_mean_ff"].agg(
    ["mean", "median", "std", "count"]
)

print("\nTA Fat Fraction Summary by Timepoint:")
print(timepoint_summary)

# Save the timepoint summary
timepoint_summary.to_csv(
    base_folder / "mri_timepoint_summary.csv"
)

# Separate TP1 and TP2
tp1 = results_df[
    results_df["timepoint"] == "TP1"
].sort_values("percent_along_muscle")

tp2 = results_df[
    results_df["timepoint"] == "TP2"
].sort_values("percent_along_muscle")

# Compare matching muscle locations between TP1 and TP2
location_change = pd.merge(
    tp1[
        [
            "percent_along_muscle",
            "distance_from_muscle_start_mm",
            "ta_mean_ff"
        ]
    ],
    tp2[
        [
            "percent_along_muscle",
            "distance_from_muscle_start_mm",
            "ta_mean_ff"
        ]
    ],
    on="percent_along_muscle",
    suffixes=("_TP1", "_TP2")
)

# Calculate the change in TA fat fraction
location_change["change_TP2_minus_TP1"] = (
    location_change["ta_mean_ff_TP2"]
    - location_change["ta_mean_ff_TP1"]
)

print("\nChange in TA Fat Fraction by Muscle Location:")
print(location_change)

# Save the location-by-location changes
location_change.to_csv(
    base_folder / "mri_fat_fraction_change_by_location.csv",
    index=False
)

# Calculate average change from TP1 to TP2
tp1_average = tp1["ta_mean_ff"].mean()
tp2_average = tp2["ta_mean_ff"].mean()
average_change = tp2_average - tp1_average

print("\nAverage TA fat fraction at TP1:", tp1_average, "%")
print("Average TA fat fraction at TP2:", tp2_average, "%")
print(
    "Average change from TP1 to TP2:",
    average_change,
    "percentage points"
)

# Plot TA fat fraction across the muscle
plt.figure()

plt.plot(
    tp1["percent_along_muscle"],
    tp1["ta_mean_ff"],
    marker="o",
    label="TP1"
)

plt.plot(
    tp2["percent_along_muscle"],
    tp2["ta_mean_ff"],
    marker="o",
    label="TP2"
)

plt.title("TA Fat Fraction Across Muscle Locations")
plt.xlabel("Percent Along Muscle (%)")
plt.ylabel("Mean TA Fat Fraction (%)")
plt.legend()
plt.tight_layout()

plt.savefig(
    base_folder / "ta_fat_fraction_across_locations.png",
    dpi=300
)

plt.show()

print("\nMRI analysis complete.")
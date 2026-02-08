# Visual Guide - Part-Based Color Selection

## Part Selection UI

### Location:
On the Customize page, right below the product preview and above the color palette.

```
┌─────────────────────────────────────────────────┐
│           Customize Your Design                 │
│                                                  │
│     [👗 Full Dress] [👔 Top] [⏳ Middle] [👖 Bottom]
│                                                  │
│     Color Palette:                              │
│     ◯ ◯ ◯ ◯ ◯                                   │
│     ◯ ◯ ◯ ◯ ◯                                   │
│                                                  │
│     Current Selection:                          │
│     Color: Red (Full Dress)                     │
│     Pattern: Solid                              │
│     Design: Classic                             │
└─────────────────────────────────────────────────┘
```

## Button States

### Default (Not Selected):
```
┌─────────────┐
│  👔 Top     │  ← White background, gray border
└─────────────┘
```

### Hover (Mouse Over):
```
┌─────────────┐
│  👔 Top     │  ← Light blue background, blue border
└─────────────┘
```

### Active (Selected):
```
╔═════════════╗
║  👔 Top     ║  ← Gradient background (purple), white text
╚═════════════╝
```

## Workflow Examples

### Example 1: Color Entire Dress Red
```
Step 1: [👗 Full Dress] ← Click here (button highlights)
Step 2: Click Red color ◯
Result: Entire dress becomes red
        Summary shows: "Red (Full Dress)"
```

### Example 2: Color Top Blue, Bottom Green
```
Step 1: [👔 Top] ← Click (button highlights)
Step 2: Click Blue color ◯
        Summary shows: "Blue (Top)"
        
Step 3: [👖 Bottom] ← Click (button highlights)
Step 4: Click Green color ◯
        Summary shows: "Green (Bottom)"
        
Preview now shows:
┌─────────────────┐
│   TOP (Blue)    │
├─────────────────┤
│  MIDDLE (orig)  │
├─────────────────┤
│ BOTTOM (Green)  │
└─────────────────┘
```

### Example 3: Multiple Parts Same Color
```
Step 1: [👔 Top] ← Click
Step 2: Click Purple ◯
        Summary: "Purple (Top)"

Step 3: [⏳ Middle] ← Click while Top is still selected
Step 4: Click Purple ◯ (same color)
        Summary: "Purple (Top, Middle)"

Step 5: [👖 Bottom] ← Deselect by clicking Top again
Step 6: Top stays Purple, Middle is Purple, Bottom is original
```

## How Each Button Works

### 👗 Full Dress Button:
```
When clicked:
  - Selects entire dress
  - Deselects any part selections
  - Color changes affect whole image
  - Summary shows: "(Full Dress)"
  
Behavior:
  - Default starting state
  - Overrides individual part selections
  - Ensures at least something is always selected
```

### 👔 Top Button:
```
When clicked:
  - Selects TOP section only
  - Deselects "Full Dress" (if it was selected)
  - Color only affects top part
  - Summary shows: "(Top)"
  
Can be combined with: Middle, Bottom
```

### ⏳ Middle Button:
```
When clicked:
  - Selects MIDDLE section only
  - Deselects "Full Dress" (if it was selected)
  - Color only affects middle part
  - Summary shows: "(Middle)"
  
Can be combined with: Top, Bottom
```

### 👖 Bottom Button:
```
When clicked:
  - Selects BOTTOM section only
  - Deselects "Full Dress" (if it was selected)
  - Color only affects bottom part
  - Summary shows: "(Bottom)"
  
Can be combined with: Top, Middle
```

## Selection Summary Display

The summary updates in real-time as you select parts and colors:

### Possibilities:
```
Full Dress Selection:
  "Red (Full Dress)"
  "Blue (Full Dress)"
  "Green (Full Dress)"

Single Part:
  "Red (Top)"
  "Blue (Middle)"
  "Green (Bottom)"

Multiple Parts:
  "Red (Top, Bottom)"
  "Blue (Top, Middle)"
  "Green (Top, Middle, Bottom)"
```

## Color Palette

All 11 colors available:

```
Row 1:  🔴 Red        🔵 Teal       🔵 Blue       🟠 Salmon     💜 Plum
Row 2:  🟡 Gold       🟢 Mint       🟠 Orange     ⚫ Gray        ⚫ Black
Row 3:  ⚪ White
```

Each color has a circle appearance and highlights when selected.

## Interaction Flow

```
START
  ↓
CUSTOMIZE PAGE
  ↓
SELECT PART:     [👗 Full] [👔 Top] [⏳ Middle] [👖 Bottom]
  ↓
CHOOSE COLOR:    [◯][◯][◯][◯][◯]
  ↓
VIEW SUMMARY:    "Red (Top)" / "Blue (Bottom)" / etc.
  ↓
CHANGE IF NEEDED ← (Loop back to SELECT PART or CHOOSE COLOR)
  ↓
SAVE DESIGN      [💾 Save to My Designs]
  ↓
END
```

## Live Updates

As you interact:
1. Click a part button → Button highlights immediately
2. Click a color → Preview updates instantly
3. Change part → Summary updates immediately
4. Change color → Preview updates instantly

No delays or lag - everything is instant!

## Example Visual Changes

### Initial State:
```
Buttons: [👗 Full Dress] [👔 Top] [⏳ Middle] [👖 Bottom]
         ↑ Highlighted
Summary: "Red (Full Dress)"
Preview: Red dress
```

### After Clicking Top Button:
```
Buttons: [👗 Full Dress] [👔 Top] [⏳ Middle] [👖 Bottom]
                         ↑ Highlighted
Summary: "Red (Full Dress)" ← Still same color, but...
Preview: Still red (no color selected for Top yet)
```

### After Clicking Blue Color:
```
Buttons: [👗 Full Dress] [👔 Top] [⏳ Middle] [👖 Bottom]
                         ↑ Highlighted
Summary: "Blue (Top)"
Preview: Top is now blue
```

### After Clicking Bottom Button:
```
Buttons: [👗 Full Dress] [👔 Top] [⏳ Middle] [👖 Bottom]
                         ↑ TWO    ↑ Highlighted
Summary: "Blue (Top, Bottom)"
Preview: Top is blue, Bottom is blue
```

### After Clicking Green Color (while Bottom selected):
```
Buttons: [👗 Full Dress] [👔 Top] [⏳ Middle] [👖 Bottom]
                         ↑ Still  ↑ Highlighted
Summary: "Green (Bottom)"
Preview: Top is still blue, Bottom is now green
```

## Tips & Tricks

✨ **Quick Color Change**:
1. Part already selected? Just click a different color
2. No need to click the part button again

✨ **Return to Full Dress**:
1. Click [👗 Full Dress] button
2. All individual selections removed
3. Back to single color for entire dress

✨ **Multiple Parts Same Color**:
1. Select first part, choose color
2. Click another part, choose same color
3. Both parts now have that color

✨ **Save Custom Design**:
1. Configure all parts the way you want
2. Click "💾 Save to My Designs"
3. Design saved with all part colors

---

## Technical Details (For Developers)

### Data Structure:
```javascript
selectedParts: {
  full: true,      // True = entire dress
  top: false,      // True = top part selected
  middle: false,   // True = middle part selected
  bottom: false    // True = bottom part selected
}

partColors: {
  top: '#FF6B6B',      // Stores color hex for top
  middle: '#FF6B6B',   // Stores color hex for middle
  bottom: '#FF6B6B'    // Stores color hex for bottom
}
```

### Key Functions:
- `selectDressPart(part)` - Toggle part selection
- `updatePartSelection()` - Update button states
- `selectColor(hex, name)` - Apply color to selected part(s)
- `applyPartialColorFilter()` - Update preview
- `updateSelectionSummary()` - Update text display

---

## Troubleshooting

**Q: Buttons not showing?**
A: Make sure you're on the Customize page. Buttons only appear there.

**Q: Parts not changing color?**
A: Make sure to click part button first, then color.

**Q: Can't change back to Full Dress?**
A: Click the [👗 Full Dress] button to reset to full selection.

**Q: Colors not visible in preview?**
A: Make sure product image loaded. Try refreshing page.

---

## Summary

This part-based color selection allows you to:
✅ Color entire dress with one color
✅ Color individual parts differently
✅ See preview update instantly
✅ Save designs with custom part colors
✅ Easy-to-use button interface
✅ Clear visual feedback

Perfect for creating custom multi-color designs!

# Quick Testing Guide - New Features

## Password Reset Feature

### To Test Password Reset:

1. **Start the application**:
   ```
   python app.py
   ```

2. **On Login Page**:
   - You'll see a new "Forgot password?" link below the password field

3. **Click "Forgot password?"**:
   - A modal dialog opens with fields for:
     - Email Address
     - New Password
     - Confirm Password

4. **Enter Your Details**:
   ```
   Email: your_registered_email@example.com
   New Password: newpass123 (minimum 6 characters)
   Confirm Password: newpass123
   ```

5. **Click "Reset Password"**:
   - System validates all fields
   - Password is updated in database
   - Success message displays
   - Modal closes automatically
   - Email field auto-fills in login form

6. **Login with New Password**:
   - Use your email and new password to login

### Validation Tests:
- ❌ Invalid email format → Error message
- ❌ Password < 6 characters → Error message
- ❌ Passwords don't match → Error message
- ✅ Valid inputs → Success message and redirect

---

## Color Selection Enhancement

### Current Implementation:

The color selection system has been enhanced to prepare for part-based coloring:

**Current Behavior** (Without UI buttons - Backend Ready):
- Click any color in the palette
- Full dress color changes
- Change is reflected in preview
- Color name updates in summary

**Future Capability** (When UI buttons added):
The backend code is ready to support selecting specific dress parts:
- Top section only
- Middle section only  
- Bottom section only
- Full dress (default)

### To Use Color Selection:

1. **Navigate to Customize Page**:
   - Select a clothing category (Women/Men)
   - Select a type (Dress, Shirt, etc.)
   - Select a specific product

2. **On Customize Page**:
   - You'll see "Color" section with color palette
   - Pattern options
   - Design style options
   - Current selection summary

3. **Change Color**:
   - Click any color circle
   - Preview updates immediately
   - Selected color name shows in "Current Selection"
   - Pattern and Design can also be changed

4. **Save Design**:
   - Click "Save to My Designs" button
   - Design saves with selected color, pattern, and style

### Color Options Available:
- Red (#FF6B6B)
- Teal (#4ECDC4)
- Blue (#45B7D1)
- Light Salmon (#FFA07A)
- Plum (#DDA0DD)
- Gold (#FFD700)
- Mint (#98D8C8)
- Orange (#F7B731)
- Gray (#888888)
- Black (#222222)
- White (#FFFFFF)

### To Add Part Selection (Optional Enhancement):

If you want to add the UI for selecting specific dress parts, add this HTML to the customize section:

```html
<div class="custom-option">
    <h3>Select Part to Color</h3>
    <div class="part-selection">
        <button class="part-selector active" id="partFull" onclick="selectDressPart('full')">Full Dress</button>
        <button class="part-selector" id="partTop" onclick="selectDressPart('top')">Top</button>
        <button class="part-selector" id="partMiddle" onclick="selectDressPart('middle')">Middle</button>
        <button class="part-selector" id="partBottom" onclick="selectDressPart('bottom')">Bottom</button>
    </div>
</div>
```

The backend JavaScript already supports this functionality!

---

## Integration Notes:

✅ **Backend Ready**: Password reset fully integrated with database
✅ **Frontend Ready**: Password reset modal fully functional
✅ **Color System**: Enhanced with part-tracking capability
✅ **Database**: Supports password updates with hashing

## API Endpoints:

### Password Reset:
```
POST /api/auth/forgot-password
POST /api/auth/reset-password
```

### Form Validation:
- Email: Must contain @ and .
- Password: Minimum 6 characters
- Confirmation: Must match password exactly

## Error Handling:

| Error | Cause | Fix |
|-------|-------|-----|
| "Invalid email format" | Email missing @ or . | Enter valid email |
| "Password must be at least 6 characters" | Short password | Use 6+ characters |
| "Passwords do not match" | Different passwords | Confirm matches password |
| "Email not found" | Email not in database | Use registered email |
| "Database error" | Server issue | Check MySQL connection |

---

## Features Summary:

✨ **Password Reset**:
- No login required
- Email-based recovery
- Database integration
- Input validation
- User-friendly interface

✨ **Color Selection**:
- Multiple color options
- Visual preview
- Part-based architecture (ready)
- Persistent design storage
- Color mapping system

---

## Troubleshooting:

**If password reset doesn't work**:
1. Check if MySQL is running
2. Verify database connection in app.py
3. Ensure user email exists in database
4. Check browser console for errors (F12)

**If colors don't change**:
1. Refresh browser
2. Clear browser cache
3. Check if preview image loaded
4. Try different color
5. Check browser console for errors

---

## Browser Console Debugging:

Press F12 to open Developer Console

Check for errors in Console tab:
- Click any color and check if `appData.currentCustomization.color` updates
- Click "Forgot password?" and check if modal opens
- Check network tab to see API requests

---

**All features are fully integrated and ready for testing!**

from django.contrib import admin
from .models import EmployeeProfile, Punch_In, Punch_Out, Total_Expense, Daily_Attendance

# Custom admin class for EmployeeProfile
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('Employee_Name','user', 'department', 'designation')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'department', 'designation')

    def Employee_Name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
# Register EmployeeProfile model with the custom admin class
admin.site.register(EmployeeProfile, EmployeeProfileAdmin)

# Custom admin class for Punch_In
class PunchInAdmin(admin.ModelAdmin):
    list_display = ('Employee_Name','user', 'date', 'time', 'vehicle_type', 'from_location', 'to_location','meter_photo')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'date', 'vehicle_type', 'from_location', 'to_location')
    list_per_page = 10

    def Employee_Name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
# Register Punch_In model with the custom admin class
admin.site.register(Punch_In, PunchInAdmin)

# Custom admin class for Punch_Out
class PunchOutAdmin(admin.ModelAdmin):
    list_display = ('Employee_Name','user', 'date', 'time', 'from_location', 'to_location')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'date', 'from_location', 'to_location')

    def Employee_Name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
# Register Punch_Out model with the custom admin class
admin.site.register(Punch_Out, PunchOutAdmin)

# Custom admin class for Total_Expense


class TotalCostAdmin(admin.ModelAdmin):
    list_display = ('Employee_Name','user', 'date', 'daily_cost', 'vehicle_type', 'punchin_from', 'punchin_to', 'punchout_from', 'punchout_to')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'date', 'vehicle_type', 'punchin_from', 'punchin_to', 'punchout_from', 'punchout_to')

    def Employee_Name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
# Register Total_Expense model with the custom admin class
admin.site.register(Total_Expense, TotalCostAdmin)

# Custom admin class for Daily_Attendance
class DailyAttendanceAdmin(admin.ModelAdmin):
    list_display = ('Employee_Name','user', 'date', 'intime', 'outtime', 'present')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'date', 'present')

    def Employee_Name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    Employee_Name.short_description = 'Employee_Name'
# Register Daily_Attendance model with the custom admin class
admin.site.register(Daily_Attendance, DailyAttendanceAdmin)


from django.contrib import admin
from django.urls import re_path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path
from app import views


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.login, name='login'),
    re_path(r'^Registration/$',views.Registration,name='Registration'),
    re_path(r'^reset_password/$', views.reset_password, name='reset_password'),

    #******************************Super Admin******************************

    #--------------------------------Amal--------------------------------
    
    re_path(r'^SuperAdmin_logout/$', views.SuperAdmin_logout, name='SuperAdmin_logout'),
    re_path(r'^SuperAdmin_Accountsett/$',views.SuperAdmin_Accountsett,name='SuperAdmin_Accountsett'),

    #------------------------------Anandhu------------------------------

    re_path(r'^SuperAdmin_index/$', views.SuperAdmin_index, name='SuperAdmin_index'),
    re_path(r'^SuperAdmin_Dashboard/$', views.SuperAdmin_Dashboard,name='SuperAdmin_Dashboard'),
    re_path(r'^SuperAdmin_Total_Instructors_Table/$',views.SuperAdmin_Total_Instructors_Table, name='SuperAdmin_Total_Instructors_Table'),
    re_path(r'^SuperAdmin_TotalTraineesUPhysicalTrainer_Table/(?P<id>\d+)/$',views.SuperAdmin_TotalTraineesUPhysicalTrainer_Table, name='SuperAdmin_TotalTraineesUPhysicalTrainer_Table'),
    re_path(r'^SuperAdmin_TraineeProfile/(?P<id>\d+)/$',views.SuperAdmin_TraineeProfile, name='SuperAdmin_TraineeProfile'),
    re_path(r'^SuperAdmin_Batch_Cards/$', views.SuperAdmin_Batch_Cards,name='SuperAdmin_Batch_Cards'),
    re_path(r'^SuperAdmin_AddBatch/$', views.SuperAdmin_AddBatch,name='SuperAdmin_AddBatch'),
    re_path(r'^SuperAdmin_ViewBatch/$', views.SuperAdmin_ViewBatch,name='SuperAdmin_ViewBatch'),
    re_path(r'^SuperAdmin_AddBatchsave/$', views.SuperAdmin_AddBatchsave,name='SuperAdmin_AddBatchsave'),
    re_path(r'^SuperAdmin_UpdateBatch/(?P<id>\d+)/$',views.SuperAdmin_UpdateBatch, name='SuperAdmin_UpdateBatch'),
    re_path(r'^SuperAdmin_UpdateBatchsave/(?P<id>\d+)/$',views.SuperAdmin_UpdateBatchsave, name='SuperAdmin_UpdateBatchsave'),
    re_path(r'^SuperAdmin_BatchDelete/(?P<id>\d+)/$',views.SuperAdmin_BatchDelete, name='SuperAdmin_BatchDelete'),

    #------------------------------Praveen------------------------------

    re_path(r'^SuperAdmin_trainees/$', views.SuperAdmin_trainees,name='SuperAdmin_trainees'),
    re_path(r'^SuperAdmin_ActiveTrainees/$',views.SuperAdmin_ActiveTrainees, name='SuperAdmin_ActiveTrainees'),
    re_path(r'^SuperAdmin_PassiveTrainees$',views.SuperAdmin_PassiveTrainees, name='SuperAdmin_PassiveTrainees'),
    re_path(r'^SuperAdmin_ActiveTraineeProfile/(?P<id>\d+)/$',views.SuperAdmin_ActiveTraineeProfile, name='SuperAdmin_ActiveTraineeProfile'),
    re_path(r'^SuperAdmin_PassiveTraineeProfile/(?P<id>\d+)/$',views.SuperAdmin_PassiveTraineeProfile, name='SuperAdmin_PassiveTraineeProfile'),
    re_path(r'^SuperAdmin_Machines/$', views.SuperAdmin_Machines,name='SuperAdmin_Machines'),
    re_path(r'^SuperAdmin_machine_category/(?P<id>\d+)/$',views.SuperAdmin_machine_category, name='SuperAdmin_machine_category'),

    #------------------------------Nimisha------------------------------

    re_path(r'^SuperAdmin_Expense/$', views.SuperAdmin_Expense,name='SuperAdmin_Expense'),
    re_path(r'^SuperAdmin_ExpenseView/$', views.SuperAdmin_ExpenseView,name='SuperAdmin_ExpenseView'),
    re_path(r'^SuperAdmin_NewTransaction/$', views.SuperAdmin_NewTransaction,name='SuperAdmin_NewTransaction'),
    re_path(r'^SuperAdmin_ExpenseViewEdit/(?P<id>\d+)$', views.SuperAdmin_ExpenseViewEdit,name='SuperAdmin_ExpenseViewEdit'),
    re_path(r'^SuperAdmin_ExpenseViewEdit_Update/(?P<id>\d+)$', views.SuperAdmin_ExpenseViewEdit_Update,name='SuperAdmin_ExpenseViewEdit_Update'),
    re_path(r'^SuperAdmin_FindExpense/$', views.SuperAdmin_FindExpense,name='SuperAdmin_FindExpense'),
    re_path(r'^SuperAdmin_FindExpense_Show/$', views.SuperAdmin_FindExpense_Show,name='SuperAdmin_FindExpense_Show'),
    re_path(r'^SuperAdmin_FindExpenseView/$', views.SuperAdmin_FindExpenseView,name='SuperAdmin_FindExpenseView'),
    re_path(r'^SuperAdmin_FindExpenseViewEdit/(?P<id>\d+)$', views.SuperAdmin_FindExpenseViewEdit,name='SuperAdmin_FindExpenseViewEdit'),
    re_path(r'^SuperAdmin_FindExpenseViewEdit_Update/(?P<id>\d+)$', views.SuperAdmin_FindExpenseViewEdit_Update,name='SuperAdmin_FindExpenseViewEdit_Update'),
    re_path(r'^SuperAdmin_FindExpenseNewTransaction/$', views.SuperAdmin_FindExpenseNewTransaction,name='SuperAdmin_FindExpenseNewTransaction'),

    #------------------------------Anwar------------------------------
     
    re_path(r'^SuperAdmin_RegistrationDetails/$',views.SuperAdmin_RegistrationDetails, name='SuperAdmin_RegistrationDetails'),
    re_path(r'^SuperAdmin_Activereg/$', views.SuperAdmin_Activereg,name='SuperAdmin_Activereg'),
    re_path(r'^SuperAdmin_newreg/$', views.SuperAdmin_newreg,name='SuperAdmin_newreg'),
    re_path(r'^Dates/(?P<id>\d+)/$', views.Dates, name='Dates'),
    re_path(r'^Active_traineesave/(?P<id>\d+)/$',views.Active_traineesave, name='Active_traineesave'),
    re_path(r'^addtopt/(?P<id>\d+)/$', views.addtopt, name='addtopt'),
    re_path(r'^addtotr/(?P<id>\d+)/$', views.addtotr, name='addtotr'),
    re_path(r'^SuperAdmin_Updatereg/(?P<id>\d+)/$',views.SuperAdmin_Updatereg, name='SuperAdmin_Updatereg'),
    re_path(r'^Active_traineeupdate/(?P<id>\d+)/$',views.Active_traineeupdate, name='Active_traineeupdate'),
    re_path(r'^Active_traineedelete/(?P<id>\d+)/$',views.Active_traineedelete, name='Active_traineedelete'),
    re_path(r'^Active_traineeaccept/(?P<id>\d+)/$',views.Active_traineeaccept, name='Active_traineeaccept'),
    re_path(r'^SuperAdmin_Passivereg/$', views.SuperAdmin_Passivereg,name='SuperAdmin_Passivereg'),
    re_path(r'^Passive_traineeupdate/(?P<id>\d+)/$',views.Passive_traineeupdate, name='Passive_traineeupdate'),
    re_path(r'^SuperAdmin_PassiveUpdate/(?P<id>\d+)/$',views.SuperAdmin_PassiveUpdate, name='SuperAdmin_PassiveUpdate'),
    re_path(r'^PassiveDates/(?P<id>\d+)/$',views.PassiveDates, name='PassiveDates'), 

    #------------------------------Akhil------------------------------
    
    re_path(r'^SuperAdmin_physical_trainer_card/$', views.SuperAdmin_physical_trainer_card, name='SuperAdmin_physical_trainer_card'),
    re_path(r'^SuperAdmin_active_trainers/$', views.SuperAdmin_active_trainers, name='SuperAdmin_active_trainers'),
    re_path(r'^Active_trainersave/(?P<id>\d+)/$', views.Active_trainersave, name='Active_trainersave'),
    re_path(r'^SuperAdmin_activetrainer_update/(?P<id>\d+)/$', views.SuperAdmin_activetrainer_update, name='SuperAdmin_activetrainer_update'),
    re_path(r'^SuperAdmin_activetrainer_update_save/(?P<id>\d+)/$', views.SuperAdmin_activetrainer_update_save, name='SuperAdmin_activetrainer_update_save'),
    re_path(r'^SuperAdmin_resigned_trainers/$', views.SuperAdmin_resigned_trainers, name='SuperAdmin_resigned_trainers'),
    re_path(r'^SuperAdmin_resignedtrainer_update/(?P<id>\d+)/$', views.SuperAdmin_resignedtrainer_update, name='SuperAdmin_resignedtrainer_update'),
    re_path(r'^SuperAdmin_resignedtrainer_update_save/(?P<id>\d+)/$', views.SuperAdmin_resignedtrainer_update_save, name='SuperAdmin_resignedtrainer_update_save'),
    re_path(r'^SuperAdmin_resignedtrainer_renew/(?P<id>\d+)/$', views.SuperAdmin_resignedtrainer_renew, name='SuperAdmin_resignedtrainer_renew'),
 
    #------------------------------Subeesh------------------------------

    re_path(r'^SuperAdmin_pay_det/$', views.SuperAdmin_pay_det, name='SuperAdmin_pay_det'),
    re_path(r'^SuperAdmin_current_trainees/$', views.SuperAdmin_current_trainees, name='SuperAdmin_current_trainees'),
    re_path(r'^SuperAdmin_previous_trainees_payment/$', views.SuperAdmin_previous_trainees_payment, name='SuperAdmin_previous_trainees_payment'),
    re_path(r'^SuperAdmin_current_trainees_payment/(?P<id>\d+)/$', views.SuperAdmin_current_trainees_payment, name='SuperAdmin_current_trainees_payment'),
    re_path(r'^SuperAdmin_current_trainees_payment_add/(?P<id>\d+)/$', views.SuperAdmin_current_trainees_payment_add, name='SuperAdmin_current_trainees_payment_add'),
    re_path(r'^SuperAdmin_current_trainees_payment_update/(?P<id>\d+)/$', views.SuperAdmin_current_trainees_payment_update, name='SuperAdmin_current_trainees_payment_update'),
    re_path(r'^SuperAdmin_current_trainees_payment_adding/(?P<id>\d+)/$', views.SuperAdmin_current_trainees_payment_adding, name='SuperAdmin_current_trainees_payment_adding'),
    re_path(r'^SuperAdmin_current_trainees_payment_verify/(?P<id>\d+)/$', views.SuperAdmin_current_trainees_payment_verify, name='SuperAdmin_current_trainees_payment_verify'),
    re_path(r'^SuperAdmin_current_trainees_payment_edit/(?P<id>\d+)/$', views.SuperAdmin_current_trainees_payment_edit, name='SuperAdmin_current_trainees_payment_edit'),
    re_path(r'^SuperAdmin_current_trainees_payment_delete/(?P<id>\d+)/$', views.SuperAdmin_current_trainees_payment_delete, name='SuperAdmin_current_trainees_payment_delete'),

    #------------------------------Sanjay------------------------------

    re_path(r'^SuperAdmin_Machine_card/$', views.SuperAdmin_Machine_card, name='SuperAdmin_Machine_card'),
    re_path(r'^SuperAdmin_Machine_addcategory/$', views.SuperAdmin_Machine_addcategory, name='SuperAdmin_Machine_addcategory'),
    re_path(r'^SuperAdmin_Machine_viewcategory/$', views.SuperAdmin_Machine_viewcategory, name='SuperAdmin_Machine_viewcategory'),
    re_path(r'^SuperAdmin_Machine_viewmachines/$', views.SuperAdmin_Machine_viewmachines, name='SuperAdmin_Machine_viewmachines'),
    re_path(r'^SuperAdmin_Machine_chestpressmachine(?P<i_id>[0-9]+)/$', views.SuperAdmin_Machine_chestpressmachine, name='SuperAdmin_Machine_chestpressmachine'),
    re_path(r'^SuperAdmin_Machine_form/$', views.SuperAdmin_Machine_form, name='SuperAdmin_Machine_form'),
    re_path(r'^SuperAdmin_add_machine/$', views.SuperAdmin_add_machine, name='SuperAdmin_add_machine'),
    re_path(r'^SuperAdmin_category1/$', views.SuperAdmin_category1, name='SuperAdmin_category1'),
    re_path(r'^SuperAdmin_Machine_bicepsview(?P<i_id>[0-9]+)/$', views.SuperAdmin_Machine_bicepsview, name='SuperAdmin_Machine_bicepsview'),

    #------------------------------Unnikrishnan------------------------------
    
    re_path(r'^superadmin_workout/$',views.superadmin_workout,name='superadmin_workout'),
    re_path(r'^superadmin_viewworkout/$',views.superadmin_viewworkout,name='superadmin_viewworkout'),
    re_path(r'^superadmin_addworkout/$',views.superadmin_addworkout,name='superadmin_addworkout'),
    re_path(r'^superadmin_tutorialpage/$',views.superadmin_tutorialpage,name='superadmin_tutorialpage'),
    re_path(r'^workout1/$',views.workout1,name='workout1'),
    re_path(r'^superadmin_addtutorial/$',views.superadmin_addtutorial,name='superadmin_addtutorial'),
    re_path(r'^superadmin_ChestDetailView(?P<i_id>[0-9]+)/$',views.superadmin_ChestDetailView,name='superadmin_ChestDetailView'),
    re_path(r'^deletevideo(?P<i_id>[0-9]+)/$',views.deletevideo,name='deletevideo'),

    #------------------------------Nidhun------------------------------ 

    re_path(r'^SuperAdmin_achievement_card/$',views.SuperAdmin_achievement_card,name="SuperAdmin_achievement_card"),
    re_path(r'^SuperAdmin_achievements_add_achievements/$',views.SuperAdmin_achievements_add_achievements,name="SuperAdmin_achievements_add_achievements"),
    re_path(r'^SuperAdmin_achievements_view_achievements/$',views.SuperAdmin_achievements_view_achievements,name="SuperAdmin_achievements_view_achievements"),
    re_path(r'^SuperAdmin_achievements_achievement_1(?P<i_id>[0-9]+)/$', views.SuperAdmin_achievements_achievement_1,name="SuperAdmin_achievements_achievement_1"),

    #******************************Trainer******************************

    #------------------------------Amal-------------------------------

    re_path(r'^Trainer_Trainees_card/$', views.Trainer_Trainees_card, name='Trainer_Trainees_card'),
    re_path(r'^Trainer_Current_Trainees_table/$', views.Trainer_Current_Trainees_table, name='Trainer_Current_Trainees_table'),
    re_path(r'^Trainer_Current_Trainees_profile/(?P<id>\d+)/$', views.Trainer_Current_Trainees_profile, name='Trainer_Current_Trainees_profile'),
    re_path(r'^Trainer_Previous_Trainees_table/$', views.Trainer_Previous_Trainees_table, name='Trainer_Previous_Trainees_table'),
    re_path(r'^Trainer_Previous_Trainees_profile/(?P<id>\d+)/$', views.Trainer_Previous_Trainees_profile, name='Trainer_Previous_Trainees_profile'),
    re_path(r'^Trainer_Accsetting/$',views.Trainer_Accsetting,name='Trainer_Accsetting'),
    re_path(r'^Trainer_Profile_Imagechange/(?P<id>\d+)/$',views.Trainer_Profile_Imagechange,name='Trainer_Profile_Imagechange'),
    re_path(r'^Trainer_Changepwd/(?P<id>\d+)/$',views.Trainer_Changepwd,name='Trainer_Changepwd'),
    re_path(r'^Trainer_logout/$',views.Trainer_logout,name='Trainer_logout'),

    #------------------------------Nidhun------------------------------

    re_path(r'^Trainer_index/$', views.Trainer_index, name='Trainer_index'),
    re_path(r'^Trainer_dashboard/$',views.Trainer_dashboard,name='Trainer_dashboard'),

    #------------------------------Anwar------------------------------

    re_path(r'^Trainer_Payment_history/$', views.Trainer_Payment_history, name='Trainer_Payment_history'),

    #------------------------------Meenu------------------------------

    re_path(r'^Trainer_workout_images/$',views.Trainer_workout_images,name='Trainer_workout_images'),
    re_path(r'^Trainer_workoutvideos1/(?P<id>\d+)/$',views.Trainer_workoutvideos1,name='Trainer_workoutvideos1'),

    #******************************Trainee******************************

    #------------------------------Amal------------------------------
    
    re_path(r'^Trainee_Accsetting/$',views.Trainee_Accsetting,name='Trainee_Accsetting'),
    re_path(r'^Trainee_logout/$', views.Trainee_logout, name='Trainee_logout'),
    re_path(r'^Trainee_Profile_Imagechange/(?P<id>\d+)/$',views.Trainee_Profile_Imagechange,name='Trainee_Profile_Imagechange'),
    re_path(r'^Trainee_Changepwd/(?P<id>\d+)/$',views.Trainee_Changepwd,name='Trainee_Changepwd'),
    
    #------------------------------unnikrishnan------------------------------

    re_path(r'^Trainee_index/$',views.Trainee_index,name='Trainee_index'),
    re_path(r'^Trainee_Dashboard/$',views.Trainee_Dashboard,name='Trainee_Dashboard'),

    #------------------------------Akhil------------------------------
  
    re_path(r'^Trainee_payment_history/$', views.Trainee_payment_history, name='Trainee_payment_history'),
    re_path(r'^Trainee_payment_save/$', views.Trainee_payment_save, name='Trainee_payment_save'),

    #------------------------------meenu------------------------------

    re_path(r'^Trainee_workout_images/$',views.Trainee_workout_images,name='Trainee_workout_images'),
    re_path(r'^Trainee_workoutvideos1/(?P<id>\d+)/$',views.Trainee_workoutvideos1,name='Trainee_workoutvideos1'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

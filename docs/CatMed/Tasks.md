- [ ] add modal doesn't work after a creation error
      
      
### New features
- Sorting by disease or other models
- list view for every related model with ability to delete, update, create
	- add the links in the sidebar
- disease list tasks
	 - [x]  inline editing
		 - [ ] weird line in the disease_form.html
		 - [ ] it widens the col
	 - [x] delete confirmation modal with alert
		 - [x] stop reloading the whole page to remove the deleted row
		 - [x] fix response rendering in the delete button(low prio)
		 - [ ] fix alerts(low prio)
		 - [x] when deleting a second object the response is being printed in the modal(mid prio) related to the first task in the subtask list
	 - [x] add modal
		 - [ ] display validation errors
	 - [x] detail list with url search params that should integrate with filters
* medicine form
	 - [x] related model is added twice to the dropdown--prevent that
		 - [x] it only works for disease
		 - [x] remove modal content after successfull add

#### Models
- [ ] change body organ to just organ
##### Later
* add the other models 
import os

with open('templates/course.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_tag = '<div class="filter-categories">'
end_tag = '</div>\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t</div>'

start_idx = content.find(start_tag)
end_idx = content.find(end_tag, start_idx)

if start_idx != -1 and end_idx != -1:
    new_html = '''<div class="filter-categories" style="width: 800px; padding: 20px;">
\t\t\t\t\t\t\t\t\t\t<form method="GET" action="{% url 'course_list' %}">
\t\t\t\t\t\t\t\t\t\t\t<div class="row clearfix">
\t\t\t\t\t\t\t\t\t\t\t\t
\t\t\t\t\t\t\t\t\t\t\t\t<!-- Column -->
\t\t\t\t\t\t\t\t\t\t\t\t<div class="column col-lg-3 col-md-6 col-sm-12">
\t\t\t\t\t\t\t\t\t\t\t\t\t<h6>Categories</h6>
\t\t\t\t\t\t\t\t\t\t\t\t\t{% for cat in categories %}
\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="form-group">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="select-box">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="checkbox" name="category" value="{{ cat.id }}" id="cat-{{ cat.id }}" {% if cat.id in selected_categories %}checked{% endif %}>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="cat-{{ cat.id }}">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<span class="default-check"></span>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<span class="check-icon fa fa-check"></span>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{{ cat.name }}
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</label>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t{% endfor %}
\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t
\t\t\t\t\t\t\t\t\t\t\t\t<!-- Column -->
\t\t\t\t\t\t\t\t\t\t\t\t<div class="column col-lg-3 col-md-6 col-sm-12">
\t\t\t\t\t\t\t\t\t\t\t\t\t<h6>Instructor</h6>
\t\t\t\t\t\t\t\t\t\t\t\t\t{% for teacher in teachers %}
\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="form-group">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="select-box">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="checkbox" name="teacher" value="{{ teacher.id }}" id="tea-{{ teacher.id }}" {% if teacher.id in selected_teachers %}checked{% endif %}>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="tea-{{ teacher.id }}">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<span class="default-check"></span>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<span class="check-icon fa fa-check"></span>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{{ teacher.name }}
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</label>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t{% endfor %}
\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t
\t\t\t\t\t\t\t\t\t\t\t\t<!-- Column -->
\t\t\t\t\t\t\t\t\t\t\t\t<div class="column col-lg-3 col-md-6 col-sm-12">
\t\t\t\t\t\t\t\t\t\t\t\t\t<h6>Sort by</h6>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="form-group">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="select-box">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="radio" name="sort" value="new" id="sort-new" {% if selected_sort == 'new' %}checked{% endif %}>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="sort-new"><span class="default-check"></span><span class="check-icon fa fa-circle"></span>New Courses</label>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="form-group">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="select-box">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<input type="radio" name="sort" value="old" id="sort-old" {% if selected_sort == 'old' %}checked{% endif %}>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<label for="sort-old"><span class="default-check"></span><span class="check-icon fa fa-circle"></span>Old Courses</label>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t\t
\t\t\t\t\t\t\t\t\t\t\t\t<!-- Column -->
\t\t\t\t\t\t\t\t\t\t\t\t<div class="column col-lg-3 col-md-6 col-sm-12">
\t\t\t\t\t\t\t\t\t\t\t\t\t<h6>Price</h6>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="form-group"><div class="select-box"><input type="checkbox" name="price" value="paid" id="price-paid" {% if 'paid' in selected_prices %}checked{% endif %}><label for="price-paid"><span class="default-check"></span><span class="check-icon fa fa-check"></span>Paid</label></div></div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="form-group"><div class="select-box"><input type="checkbox" name="price" value="free" id="price-free" {% if 'free' in selected_prices %}checked{% endif %}><label for="price-free"><span class="default-check"></span><span class="check-icon fa fa-check"></span>Free</label></div></div>
\t\t\t\t\t\t\t\t\t\t\t\t\t
\t\t\t\t\t\t\t\t\t\t\t\t\t<br>
\t\t\t\t\t\t\t\t\t\t\t\t\t<h6>Level</h6>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="form-group"><div class="select-box"><input type="checkbox" name="level" value="Beginner" id="level-beg" {% if 'Beginner' in selected_levels %}checked{% endif %}><label for="level-beg"><span class="default-check"></span><span class="check-icon fa fa-check"></span>Beginner</label></div></div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="form-group"><div class="select-box"><input type="checkbox" name="level" value="Intermediate" id="level-int" {% if 'Intermediate' in selected_levels %}checked{% endif %}><label for="level-int"><span class="default-check"></span><span class="check-icon fa fa-check"></span>Intermediate</label></div></div>
\t\t\t\t\t\t\t\t\t\t\t\t\t<div class="form-group"><div class="select-box"><input type="checkbox" name="level" value="Expert" id="level-exp" {% if 'Expert' in selected_levels %}checked{% endif %}><label for="level-exp"><span class="default-check"></span><span class="check-icon fa fa-check"></span>Expert</label></div></div>
\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t\t<div class="form-group" style="margin-top:20px;">
\t\t\t\t\t\t\t\t\t\t\t\t<button type="submit" class="theme-btn btn-style-two"><span class="txt">Apply Filters</span></button>
\t\t\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t\t\t</form>
'''
    content = content[:start_idx] + new_html + content[end_idx:]
    with open('templates/course.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated filter section in course.html')
else:
    print('Indices not found:', start_idx, end_idx)

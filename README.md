## Try Django2.0 and django-mptt
This is my plain project start by bare hand w/o boilerplates assist
Because I want to get `mptt` up to speed as soon as possible, but
this time it is very early(3 days after Dj2 released)


<ul class="root">
    {% recursetree nodes %}
    <div style="color: purple">
        Root: {{node.name}}
    </div>
    {% if not node.is_leaf_node %}
        <ul style="color:cyan">
            2nd: {{children}}
        </ul>
    {% elif node.is_child_node %}
        <ul style="color:gray">
            test: {{children}}
        </ul>
    {% endif %}
    {% endrecursetree %}
</ul>


<ul class="
{% if not node.is_leaf_node and not node.is_root_node and node.is_child_node %}
child_parent
{% elif node.is_leaf_node and not node.is_root_node %}
leaf_node
{% endif %}">

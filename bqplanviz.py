#!/usr/bin/env python2

import sys
import json

from jinja2 import Template


TEMPLATE = '''
digraph G {
    graph [fontsize=30];
    ratio = auto;
    {% for stage in queryPlan %}
        "{{ stage.id }}" [ shape = "Mrecord" label = <
            <table border="0">
                <tr><td border="1" bgcolor="lightgray">{{ stage.name }}</td></tr>
                {% for step in stage.steps %}
                    <tr><td border="1">{{ step.kind }}</td></tr>
                    {% for substep in step.substeps %}
                        <tr><td align="left">{{ substep }}</td></tr>
                    {% endfor %}
                {% endfor %}
            </table>
        > ];
        {% for inputStage in stage.inputStages  %}
        "{{ inputStage }}" -> "{{ stage.id }}";
        {% endfor %}
    {% endfor %}
}
'''


def main():
    plan_file = _get_input()
    out_file = _get_output()
    plan = json.load(plan_file)
    plan_dot = bq_plan_to_dot(plan['statistics']['query'])
    out_file.write(plan_dot)
    plan_file.close()
    out_file.close()


def _get_input():
    if len(sys.argv) > 1:
        return open(sys.argv[1])
    else:
        return sys.stdin


def _get_output():
    if len(sys.argv) > 2:
        return open(sys.argv[2], "w")
    elif len(sys.argv) > 1:
        return open(sys.argv[1]+".dot", "w")
    else:
        return sys.stdout


def bq_plan_to_dot(plan):
    template = Template(TEMPLATE)
    return template.render(plan)


if __name__ == '__main__':
    main()
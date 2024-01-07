from manim import *

class DataGraph(Scene):
    graph_data = []
    
    config.media_dir="reports"
    
    def __init__(self, graph_data, **kwargs):
        # max 100+1 data points
        step = int(len(graph_data)/100) if len(graph_data)>=100 else 1
        self.graph_data = graph_data[::step]
        
        # Always contain last data tuple
        if self.graph_data[-1] != graph_data[-1]:
            self.graph_data.append(graph_data[-1])
        
        super().__init__(**kwargs)
    
    def construct(self):
        first_y = self.graph_data[0][1]
        last_y = self.graph_data[len(self.graph_data)-1][1]
        
        if last_y >= first_y:
            final_val = last_y
            starting_val = first_y
        else:
            final_val = first_y
            starting_val = last_y
        
        # TODO fix 'maximum size exceeded' for a^3-(500*a)^2 - is a*500^2 too big?
        plane = NumberPlane(
            x_range = (1, self.graph_data[-1][0], int(self.graph_data[-1][0] / 10)),
            y_range = (starting_val, final_val, (abs(final_val - starting_val) / 10)),
            x_length = 10,
            y_length = 5.625,
            axis_config={"include_numbers": True},
            y_axis_config={
                "label_direction": LEFT,
                #"decimal_number_config": {"num_decimal_places": 2}
                },
        )
        plane.center()
        
        labels = plane.get_axis_labels(
            Tex("Iteration").scale(0.6), Tex("Result").scale(0.6)
        )
        
        xs = [tup[0] for tup in self.graph_data]
        ys = [tup[1] for tup in self.graph_data]
        xs = [float(x) for x in xs]
        ys = [float(y) for y in ys]

        
        line_graph = plane.plot_line_graph(
            x_values=xs, 
            y_values=ys,
            line_color=GOLD_E,
            stroke_width = 3,
            add_vertex_dots=False
        )
        
        last_point_label = Tex(f"Final generation = ({xs[-1]}, {ys[-1]})").scale(0.6)
        last_point_label.next_to(line_graph, 2*UP, buff=0.1)
        
        animations = [
            Create(line_graph, run_time=8),
            FadeIn(last_point_label),
        ]
        
        # debugging (this will be removed)
        #print(first_y, last_y)
        #print(1, len(self.graph_data))
        
        self.add(plane, labels)
        self.play(AnimationGroup(*animations, lag_ratio=1))
        self.wait(duration=3)
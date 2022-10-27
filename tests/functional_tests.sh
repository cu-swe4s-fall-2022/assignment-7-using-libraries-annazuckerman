test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# functional tests for plotter.py
wget -O iris.data \
"https://raw.githubusercontent.com/cu-swe4s-fall-2022/assignment-7-using-libraries-annazuckerman/main/iris.data"

run test_plotter python plotter.py \
    --filename iris.data \
    --box_outfile iris_boxplot.png \
    --scatter_outfile petal_width_v_length_scatter.png \
    --multipanel_outfile multi_panel_figure.png

curr_dir=$(pwd)
file1='/iris_boxplot.png'
file2='/petal_width_v_length_scatter.png'
file3='/multi_panel_figure.png'
path1=$curr_dir$file1
path2=$curr_dir$file2
path3=$curr_dir$file3
assert_in_stdout 'Output plot saved to: '$path1
assert_in_stdout 'Output plot saved to: '$path1
assert_in_stdout 'Output plot saved to: '$path1
# check that the output file actually exists
if [ -f "$path1" ]; then
    echo ' TEST SUCCEEDED: boxplot found in expected location.'
else
    echo ' TEST FAILED: boxplot not found in expected location!'
fi
if [ -f "$path2" ]; then
    echo ' TEST SUCCEEDED: scatterplot found in expected location.'
else
    echo ' TEST FAILED: scatterplot not found in expected location!'
fi
if [ -f "$path3" ]; then
    echo ' TEST SUCCEEDED: multipanel plot found in expected location.'
else
    echo ' TEST FAILED: multipanel plot not found in expected location!'
fi

assert_exit_code 0

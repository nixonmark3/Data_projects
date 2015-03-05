__author__ = 'noelbell'

# find all deltaT in JetA dataframe

# based on Alper's flint_hills2.py
# flooding events are identified in column "flood_events" and start and end with value of 9.5.  there are 8 pairs

import pandas as pd
import bokeh.plotting as plt
import bokeh.models as plt_models
#import pymongo_wrapper as py_wrap



def find_events(data):
    events = data[data['flood_events'] > 0]

    # print(events)

    series = events['flood_events']
    print(series)
    all_events = [x for x in zip(series.index, series)]
    print(' all events........\n',all_events)
    filtered_events = []
    pt = all_events[0][0]
    print('..pt..\n',pt)
    print('...pt.date = ',pt.date())
    for event in all_events:
        if len(filtered_events) == 0:
            filtered_events.append(event)
        #elif pt.date() != event[0].date():
         #   filtered_events.append(event)
        else: # pt.date() != event[0].date():  NOTE  :  we don't care if 2nd item is on same day
            filtered_events.append(event)
        pt = event[0]
    print('...filtered events....',filtered_events)
    return filtered_events


def create_figure_for_tag(df_events, df, tag_name):

    title_text = 'Jet Flood - ' + str(tag_name)

    fig = plt.figure(title=title_text, tools= "hover,pan,wheel_zoom,box_zoom,reset,resize",
                x_axis_label="Time", y_axis_label=tag_name, plot_width=1400, plot_height=600,
                x_axis_type="datetime", y_range=plt_models.Range1d(start=df[tag_name].min(),
                end=df[tag_name].max()))

    x = df.index.values

    fig.line(x, df[tag_name], legend=tag_name, color='#00CC00', line_dash=[1, 4])
    fig.line(x, df_events['flood_events'], color='red', line_dash=[1, 4],y_range_name='right axis')

    mean = df[tag_name].mean()
    std = df[tag_name].std()

    s = pd.Series([(std * 2) + mean] * len(df[tag_name]), index=df[tag_name].index)
    #fig.line(x, s.values, legend='Std*2', color='#9900FF', line_dash=[4, 4])

    s = pd.Series([mean] * len(df[tag_name]), index=df[tag_name].index)
    ##fig.line(x, s.values, legend='Mean', color='#9900FF', line_dash=[4, 4])

    s = pd.Series([(std * -2) + mean] * len(df[tag_name]), index=df[tag_name].index)
    #fig.line(x, s.values, legend='-Std*2', color='#9900FF', line_dash=[4, 4])

    # plot flooding events
    #fig.extra_y_ranges = {'right axis': plt_models.Range1d(start=0, end=10)}
    ###
    # fig.line(x, df[event], legend=event, color='red', line_cap='round',y_range_name='right axis')

    #fig.add_layout(plt_models.LinearAxis(y_range_name='right axis'), 'right')


    fig.extra_y_ranges = {'right axis': plt_models.Range1d(start=0, end=10)}
    #fig.line(x, df['10P1019'], legend='10P1019', color='#0000FF', line_dash=[1, 4], y_range_name='right axis 10P1019')

    event_labels = list()
    event_x_axis = list()
    event_y_axis = list()

    for i, (x, y) in enumerate(find_events(df_events)):
        event_labels.append('E{0}'.format(i + 1))
        event_x_axis.append(x)
        event_y_axis.append(y)
    #
    fig.diamond(event_x_axis[0:2], event_y_axis[0:2], color='red', fill_alpha=0.2, size=5, y_range_name='right axis', legend='June23-25')

    fig.diamond(event_x_axis[2:4], event_y_axis[2:4], color='blue', fill_alpha=0.2, size=5, y_range_name='right axis', legend='July6-7')
    fig.diamond(event_x_axis[4:6], event_y_axis[4:6], color='black', fill_alpha=0.2, size=5, y_range_name='right axis', legend='July11-12')
    fig.diamond(event_x_axis[6:8], event_y_axis[6:8], color='orange', fill_alpha=0.2, size=5, y_range_name='right axis', legend='July26-27')
    fig.circle(event_x_axis[8:10], event_y_axis[8:10], color='red', fill_alpha=0.2, size=5, y_range_name='right axis', legend='Aug24')
    fig.circle(event_x_axis[10:12], event_y_axis[10:12], color='blue', fill_alpha=0.2, size=5, y_range_name='right axis', legend='Sept1-3')
    fig.circle(event_x_axis[12:14], event_y_axis[12:14], color='black', fill_alpha=0.2, size=5, y_range_name='right axis', legend='Sept7-8')
    fig.circle(event_x_axis[14:16], event_y_axis[14:16], color='orange', fill_alpha=0.2, size=5, y_range_name='right axis', legend='Sept16-18')


    fig.line(event_x_axis[0:2], event_y_axis[0:2], color='red',  size=5, y_range_name='right axis')
    fig.line(event_x_axis[2:4], event_y_axis[2:4], color='blue', size=5, y_range_name='right axis')
    fig.line(event_x_axis[4:6], event_y_axis[4:6], color='black',size=5, y_range_name='right axis')
    fig.line(event_x_axis[6:8], event_y_axis[6:8], color='orange',size=5, y_range_name='right axis')
    fig.line(event_x_axis[8:10], event_y_axis[8:10], color='red', size=5, y_range_name='right axis')
    fig.line(event_x_axis[10:12], event_y_axis[10:12], color='blue', size=5, y_range_name='right axis')
    fig.line(event_x_axis[12:14], event_y_axis[12:14], color='black', size=5, y_range_name='right axis')
    fig.line(event_x_axis[14:16], event_y_axis[14:16], color='orange',size=5, y_range_name='right axis')
    #fig.text(event_x_axis, event_y_axis, text=event_labels, alpha=0.5, text_font_size="8pt", text_baseline="middle", text_align="center", y_range_name='right axis')
    #
    fig.add_layout(plt_models.LinearAxis(y_range_name='right axis'), 'right')

    return fig


def main():
#    df = py_wrap.load_data_set()
    df = pd.read_csv('/volumes//Macintosh HD/Users/noelbell/Documents/big_data/Flooding Data/June-Sept2009_df_events.csv', parse_dates=True, index_col=0)



    tags = [x for x in df.columns[1:] if ('TC'in x) or ('TI' in x)]
    print('tags = ', tags)
    tags.remove('18TC318.PV')
    t_tags = [x for x in tags if 'PV' in x]
    print('t_tags', t_tags )

    data_dict = dict()
    for tag in t_tags:
         data_dict[tag+'-TC318'] = (df[tag] - df['18TC318.PV'])
    deltat_data = pd.DataFrame(data_dict)
    # data['sum'] = data.sum(axis=1)
    # data['sum_mean'] = pd.rolling_mean(data['sum'], 300)
    # data['sum_ewm_20'] = pd.ewma(data['sum'], 20)
    # data['sum_ewm_50'] = pd.ewma(data['sum'], 50)


    #tags = ['18AI010.PV']
    tags = deltat_data.columns.values

    for tag in tags:
         plt.output_file('/volumes//Macintosh HD/Users/noelbell/Documents/big_data/Flooding Data/suncor_jetflood_dt_plots/{0}.html'.format(tag), title='{0}'.format(tag))
         fig1 = create_figure_for_tag(df, deltat_data, tag)
         plot = plt.gridplot([[fig1]])
         plt.save(obj=plot)


if __name__ == "__main__":
    main()
import datetime as dt
from BackfillOperator import backfill_operator

run_count_1 = 0
run_count_2 = 0
run_count_3 = 0
run_count_4 = 0
run_count_5 = 0
delta_second_1 = 10

def test_run_one_time_when_delay_in_range():

    @backfill_operator(max_run=1, min_data_lag_to_stop=dt.timedelta(seconds=10))
    def my_etl_func():

        global run_count_1
        run_count_1 += 1
        return dt.timedelta(seconds=1)

    my_etl_func()
    assert run_count_1 == 1


def test_run_ten_times_when_delay_out_of_range():

    @backfill_operator(max_run=10, min_data_lag_to_stop=dt.timedelta(seconds=10))
    def my_etl_func():

        global run_count_2
        run_count_2 += 1
        return dt.timedelta(seconds=20)

    my_etl_func()
    assert run_count_2 == 10


def test_should_run_max_ten_times_if_cant_catch_up():

    @backfill_operator(max_run=10, min_data_lag_to_stop=dt.timedelta(seconds=10))
    def my_etl_func():

        global run_count_3
        run_count_3 += 1
        return dt.timedelta(seconds=15)

    my_etl_func()
    assert run_count_3 <= 10

def test_should_run_ten_times_as_default():

    @backfill_operator()
    def my_etl_func():

        global run_count_4
        run_count_4 += 1
        return dt.timedelta(seconds=30)

    my_etl_func()
    assert run_count_4 == 10

def test_should_run_five_times_if_can_catchup():

    @backfill_operator(max_run=10, 
        min_data_lag_to_stop=dt.timedelta(seconds=5), 
        latest_time_for_rerun=dt.timedelta(seconds=1 + 100))
    def my_etl_func():

        global run_count_5
        global delta_second_1
        run_count_5 += 1
        delta_second_1 -= 1
        return dt.timedelta(seconds=delta_second_1)

    my_etl_func()
    assert run_count_5 == 5

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import internal_unit_testing

from . import airflow_db_cleanup


def test_version_comparison():
    # b/408307862 - Validate version check logic used in the sample.
    AIRFLOW_VERSION = airflow_db_cleanup.parse_airflow_version("2.10.5+composer")

    assert AIRFLOW_VERSION == (2, 10, 5)
    assert AIRFLOW_VERSION > (2, 9, 1)

    AIRFLOW_VERSION = airflow_db_cleanup.parse_airflow_version("2.9.2")

    assert AIRFLOW_VERSION == (2, 9, 2)
    assert AIRFLOW_VERSION < (2, 9, 3)


def test_dag_import():
    """Test that the DAG file can be successfully imported.

    This tests that the DAG can be parsed, but does not run it in an Airflow
    environment. This is a recommended confidence check by the official Airflow
    docs: https://airflow.incubator.apache.org/tutorial.html#testing
    """
    from . import airflow_db_cleanup as module

    internal_unit_testing.assert_has_valid_dag(module)

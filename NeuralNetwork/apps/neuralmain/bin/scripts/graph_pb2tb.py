#!/usr/bin/python
#
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

import tensorflow as tf


def load_graph(graph_pb_path):
    """
    Args:
        graph_pb_path: path to graph
    """
    with open(graph_pb_path, 'rb') as f:
        content = f.read()
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(content)
    with tf.Graph().as_default() as graph:
        tf.import_graph_def(graph_def, name='')
    return graph


def graph_to_tensorboard(graph, out_dir):
    """
  Args:
      graph: graph
      out_dir: name of output folder
  """
    with tf.Session():
        train_writer = tf.summary.FileWriter(out_dir)
        train_writer.add_graph(graph)


def main(out_dir, graph_pb_path):
    """
    Args:
        out_dir: name of output folder
        graph_pb_path: path to graph
    """
    graph = load_graph(graph_pb_path)
    graph_to_tensorboard(graph, out_dir)


if __name__ == "__main__":
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    main(*sys.argv[1:])

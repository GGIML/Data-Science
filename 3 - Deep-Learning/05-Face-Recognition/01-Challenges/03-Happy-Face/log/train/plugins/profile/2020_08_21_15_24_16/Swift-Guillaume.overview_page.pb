�	P�� ��@P�� ��@!P�� ��@	(�7�?(�7�?!(�7�?"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$P�� ��@�[�tYL�?A���>Š�@Y�D�
)�?*	�G�z~Z@2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat������?!�
E�@@)?8�:V)�?1!*p��:@:Preprocessing2F
Iterator::Model����˥?!���D@)��&N�?1᳢]�6@:Preprocessing2U
Iterator::Model::ParallelMapV29�3Lm��?!@7=�2@)9�3Lm��?1@7=�2@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMap(|���?!���,�(5@)�����ڐ?1T�Ƚ/@:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensor~6rݔ�z?!i�g�\�@)~6rݔ�z?1i�g�\�@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::TensorSliceE�Ɵ�lx?!�c`"�@)E�Ɵ�lx?1�c`"�@:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zip�^���:�?!p
H��M@)���v�>x?1-�͚�W@:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 0.0% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no9(�7�?#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	�[�tYL�?�[�tYL�?!�[�tYL�?      ��!       "      ��!       *      ��!       2	���>Š�@���>Š�@!���>Š�@:      ��!       B      ��!       J	�D�
)�?�D�
)�?!�D�
)�?R      ��!       Z	�D�
)�?�D�
)�?!�D�
)�?JCPU_ONLYY(�7�?b Y      Y@q����~?"�
device�Your program is NOT input-bound because only 0.0% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*�
�<a href="https://www.tensorflow.org/guide/data_performance_analysis" target="_blank">Analyze tf.data performance with the TF Profiler</a>*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2I
=type.googleapis.com/tensorflow.profiler.GenericRecommendation
nono:
Refer to the TF2 Profiler FAQ2"CPU: B 
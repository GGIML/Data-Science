?	??w??T?@??w??T?@!??w??T?@	??????????????!???????"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$??w??T?@?Ց#????Anlv??S?@Y$+?ƈ??*	??~j??R@2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeatEկt><??!0f?rN?A@)?f????1dQX1{<@:Preprocessing2F
Iterator::Model?E{????!??cZD@)l%t??Y??1????%b6@:Preprocessing2U
Iterator::Model::ParallelMapV2AJ?i??!?s?#??1@)AJ?i??1?s?#??1@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMap???$????!݆c?y2@)?a?[>???1??)eB?'@:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensor0?Qd??t?!??5??@)0?Qd??t?1??5??@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::TensorSlicep???$t?!???ô?@)p???$t?1???ô?@:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zip?dp??:??!P?`???M@)??"???s?1儀?K@:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 0.0% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no9???????#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	?Ց#?????Ց#????!?Ց#????      ??!       "      ??!       *      ??!       2	nlv??S?@nlv??S?@!nlv??S?@:      ??!       B      ??!       J	$+?ƈ??$+?ƈ??!$+?ƈ??R      ??!       Z	$+?ƈ??$+?ƈ??!$+?ƈ??JCPU_ONLYY???????b Y      Y@q?D1sx-|?"?
device?Your program is NOT input-bound because only 0.0% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*?
?<a href="https://www.tensorflow.org/guide/data_performance_analysis" target="_blank">Analyze tf.data performance with the TF Profiler</a>*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2I
=type.googleapis.com/tensorflow.profiler.GenericRecommendation
nono:
Refer to the TF2 Profiler FAQ2"CPU: B 
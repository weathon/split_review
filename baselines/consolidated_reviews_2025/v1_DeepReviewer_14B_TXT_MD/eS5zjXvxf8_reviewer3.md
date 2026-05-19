### Summary

The paper introduces MultiIoT, a comprehensive benchmark for the Internet of Things (IoT) that encompasses over 1.15 million samples from 12 different modalities and 8 tasks. MultiIoT addresses challenges such as learning from multiple sensory modalities, capturing fine-grained interactions over extended temporal ranges, and managing the extreme heterogeneity found in real-world sensor data. The paper also presents a set of robust modeling baselines, ranging from modality and task-specific methods to multisensory and multitask models, aiming to foster further research in multisensory representation learning for IoT applications.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces MultiIoT, a comprehensive benchmark for IoT, covering a wide range of real-world sensory modalities and tasks. This is a valuable contribution to the field, as it provides a standardized framework for evaluating machine learning models in IoT scenarios.

2. The paper addresses key challenges in IoT data processing, including learning from multiple sensory modalities, capturing fine-grained interactions over extended temporal ranges, and managing the extreme heterogeneity found in real-world sensor data. These are critical issues that need to be tackled for effective IoT applications.

3. The paper presents a set of robust modeling baselines, ranging from modality and task-specific methods to multisensory and multitask models. This provides a solid foundation for future research in multisensory representation learning for IoT.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the specific machine learning techniques used in the modeling baselines. Providing more information about the architectures, training procedures, and hyperparameter settings would enhance the reproducibility and understanding of the results. For example, the paper mentions using CNNs for image data, but it does not specify the exact CNN architecture (e.g., ResNet, VGG), the number of layers, filter sizes, or activation functions. Similarly, for time-series data, it is unclear whether recurrent neural networks (RNNs), LSTMs, or Transformers were used, and what their specific configurations were. This lack of detail makes it difficult to assess the validity of the baselines and to build upon them.

2. While the paper mentions the release of the MultiIoT benchmark, it could provide more details about the data collection process, the data format, and the tools and resources available for researchers. This would facilitate the adoption and use of the benchmark by the broader research community. For instance, information about the sampling rates of different sensors, the synchronization method used across modalities, and the specific hardware used for data acquisition is missing. Furthermore, the paper does not specify the format of the released data (e.g., CSV, HDF5), the structure of the files, or the naming conventions used. The absence of these details hinders the ease of use of the benchmark.

3. The paper could explore the potential applications of MultiIoT in more detail. Providing concrete examples of how the benchmark can be used to address real-world IoT challenges would further highlight its significance and impact. While the paper mentions applications like smart homes and healthcare, it does not provide specific scenarios or use cases that demonstrate how the benchmark can be used to solve practical problems. For example, it would be beneficial to show how MultiIoT can be used to develop a system for activity recognition in smart homes or for patient monitoring in healthcare settings.

### Suggestions

To enhance the paper, the authors should provide a comprehensive description of the modeling baselines, including the specific architectures, training procedures, and hyperparameter settings. For example, when using CNNs for image data, the authors should specify the exact architecture (e.g., ResNet-50, VGG-16), the number of layers, filter sizes, activation functions, and optimization algorithms. For time-series data, they should detail whether RNNs, LSTMs, or Transformers were used, along with their specific configurations, such as the number of layers, hidden units, and attention mechanisms. Furthermore, the authors should include details about the training procedures, such as the batch size, learning rate, and the number of training epochs. This level of detail is crucial for reproducibility and for other researchers to build upon the presented work. The authors should also include a table summarizing the hyperparameter settings for each baseline model.

In addition, the authors should provide a detailed description of the MultiIoT benchmark, including the data collection process, the data format, and the tools and resources available for researchers. This should include information about the sampling rates of different sensors, the synchronization method used across modalities, and the specific hardware used for data acquisition. The authors should also specify the format of the released data (e.g., CSV, HDF5), the structure of the files, and the naming conventions used. Furthermore, they should provide a README file with clear instructions on how to download, preprocess, and use the data. The authors could also consider providing a software toolkit with functions for data loading, preprocessing, and visualization, which would greatly facilitate the adoption of the benchmark by the research community. This would make the benchmark more accessible and useful for a wider range of researchers.

Finally, the authors should provide more concrete examples of how MultiIoT can be used to address real-world IoT challenges. This could include specific scenarios or use cases that demonstrate how the benchmark can be used to develop practical solutions. For example, the authors could show how MultiIoT can be used to develop a system for activity recognition in smart homes, where data from different sensors (e.g., cameras, motion detectors, microphones) is used to identify the activities of residents. Another example could be patient monitoring in healthcare settings, where data from wearable sensors is used to track vital signs and detect anomalies. These examples would help to highlight the significance and impact of the benchmark and would encourage researchers to use it for their own research.

### Questions

1. Could the authors provide more details about the specific machine learning techniques used in the modeling baselines, including the architectures, training procedures, and hyperparameter settings?

2. Could the authors elaborate on the data collection process for the MultiIoT benchmark, including the data format, the tools and resources available for researchers, and any potential biases or limitations of the dataset?

3. How do the authors envision the application of MultiIoT in real-world scenarios, and what are the potential challenges and opportunities associated with its deployment?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

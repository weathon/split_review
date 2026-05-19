### Summary

This paper introduces MultiIoT, a large-scale benchmark for multisensory learning in the Internet of Things (IoT). MultiIoT comprises over 1.15 million samples across 12 modalities and 8 tasks, addressing challenges in learning from diverse sensory data, capturing long-range temporal interactions, and handling heterogeneity in real-world sensors. The authors also provide a set of modeling baselines, ranging from modality-specific to multisensory and multitask models, to facilitate future research in this area.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The introduction of MultiIoT as a large-scale benchmark is a significant contribution, providing a comprehensive dataset for multisensory IoT research.
2. The paper addresses critical challenges in IoT data processing, such as handling diverse modalities, long-range temporal dependencies, and sensor heterogeneity.
3. The inclusion of various modeling baselines offers a valuable starting point for researchers and highlights the complexities of multisensory IoT data.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the specific machine learning techniques used in the modeling baselines. While the paper mentions the use of CNNs for image data and RNNs for time-series data, it lacks specifics on the architectures, training procedures, and hyperparameter settings. For instance, what specific type of CNN (e.g., ResNet, VGG) was used? What were the learning rates, batch sizes, and optimization algorithms? This level of detail is crucial for reproducibility and for other researchers to build upon the presented work.
2. While the paper mentions the release of the MultiIoT benchmark, it could provide more details about the data collection process, the data format, and the tools and resources available for researchers. For example, what was the sampling rate for each sensor modality? How were the different modalities synchronized? What preprocessing steps were applied to the raw data? This information is essential for researchers to effectively use the benchmark.
3. The paper could explore the potential applications of MultiIoT in more detail. While the tasks are relevant, the paper could provide more concrete examples of how the benchmark can be used to address real-world IoT challenges. For instance, how could MultiIoT be used to improve the accuracy of activity recognition in smart homes or to enhance the reliability of industrial automation systems? Providing such examples would further highlight the significance and impact of the benchmark.

### Suggestions

To enhance the paper, the authors should provide a more detailed description of the modeling baselines. This should include the specific architectures used for each modality (e.g., CNN, RNN, Transformer), the training procedures (e.g., optimization algorithm, learning rate, batch size), and the hyperparameter settings. For example, if a CNN was used for image data, the authors should specify the exact architecture (e.g., ResNet-50, VGG-16), the number of layers, the filter sizes, and the activation functions. Similarly, for time-series data, they should detail whether RNNs, LSTMs, or Transformers were used, along with their specific configurations. This level of detail is crucial for reproducibility and for other researchers to build upon the presented work. Furthermore, the authors should include a table summarizing the hyperparameter settings for each baseline model, which would greatly facilitate the use of the benchmark.

In addition, the authors should provide a comprehensive description of the MultiIoT benchmark, including the data collection process, the data format, and the tools and resources available for researchers. This should include information about the sampling rates of different sensors, the synchronization method used across modalities, and the specific hardware used for data acquisition. The authors should also specify the format of the released data (e.g., CSV, HDF5), the structure of the files, and the naming conventions used. Furthermore, they should provide a README file with clear instructions on how to download, preprocess, and use the data. The authors could also consider providing a software toolkit with functions for data loading, preprocessing, and visualization, which would greatly facilitate the adoption of the benchmark by the research community. This would make the benchmark more accessible and useful for a wider range of researchers.

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

### Summary

The paper proposes retrieval-augmented test-time adaptation (RA-TTA) for adapting vision-language models to test distribution using external knowledge obtained from a web-scale image database. RA-TTA uses fine-grained text descriptions both for retrieving proper external images and refining VLMs’ predictions with the retrieved external images. Extensive evaluations on 17 datasets validate that RA-TTA outperforms the state-of-the-art methods by 2.49-8.45% on average.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple but effective.
- The experimental results are convincing.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method requires a web-scale image database for retrieval, which may be hard to obtain in real applications.
- The proposed method requires generating text descriptions for each class, which can be expensive when the number of classes is large.
- The proposed method requires calculating the alignment scores between a test image and the text descriptions in the database, which can be computationally expensive when the database is large.

### Suggestions

The reliance on a web-scale image database is a significant practical limitation. While the authors argue that such databases are becoming common, the cost of storing and maintaining such a large database, not to mention the computational resources needed for frequent access, remains a substantial hurdle for many research groups and practical applications. The paper should include a more detailed discussion of the trade-offs between database size and performance, and explore methods to mitigate the computational burden of retrieval, such as using approximate nearest neighbor search or hierarchical indexing. Furthermore, the paper should investigate the impact of database quality on the final performance, as a noisy or biased database could negatively affect the adaptation process. It would be beneficial to see experiments with databases of varying sizes and quality to better understand the practical limitations of the proposed approach.

The process of generating text descriptions for each class, while potentially parallelizable, still introduces a non-negligible overhead, especially when dealing with a large number of classes. The paper should provide a more detailed analysis of the time and resources required for this step, and explore alternative methods for obtaining class descriptions, such as using existing knowledge bases or leveraging the capabilities of large language models to generate descriptions in a more efficient manner. The authors should also consider the potential for errors or biases in the generated descriptions and how these might affect the overall performance of the method. A sensitivity analysis of the quality of the text descriptions on the final performance would be valuable.

The computational cost of calculating alignment scores between a test image and the text descriptions in the database is a major concern, particularly as the database size increases. The paper should explore more efficient methods for calculating these scores, such as using approximate nearest neighbor search or dimensionality reduction techniques. The authors should also investigate the impact of the number of retrieved images on the final performance, as retrieving a large number of images may not be necessary and could lead to increased computational cost without significant gains in accuracy. A detailed analysis of the computational complexity of the proposed method, including the time and memory requirements for each step, is essential for assessing its practical feasibility.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

4

**********

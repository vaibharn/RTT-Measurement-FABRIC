# RTT-Measurement-FABRIC
Measuring RTT using different methods on FABRIC and comparing them.

This paper presents a comprehensive study of Round-Trip Time (RTT) within the intricate framework of the FABRIC testbed network. RTT, a fundamental metric of network performance, serves as a crucial determinant of user experience and the overall quality of a network. This study explores the facets of RTT, delving into its impact on user satisfaction and network efficiency. To achieve these objectives, various RTT measurement methods are compared and employed. These methods include One-way Latency (OWL) utilizing Precision Time Protocol (PTP), a novel algorithm implemented in the data plane using P4 programmable high-performance BMv2 switches, continuous TCP traffic analysis, and the traditional UNIX "ping" command. This study provides a nuanced understanding of RTT measurement behaviors by leveraging these diverse techniques.


FABRIC Architecture:
![image](https://github.com/vaibharn/RTT-Measurement-FABRIC/assets/30080510/994f5d66-02ca-494f-8f84-10d6d5b3d9e4)


Results:
![image](https://github.com/vaibharn/RTT-Measurement-FABRIC/assets/30080510/c0e29ff4-1b73-46a0-8676-1dc2438bf2ec)

Insights gained:
After the experiment is performed, the results from the different methods will be tabulated and compared, and medians of sufficiently large observations will be taken for visualization and analysis.
 
Initial observations point toward the fact that the RTT values from the OWL method are slightly smaller than that of  ping. However, there are a few cases where the opposite is true. This finding might indicate OWL is a more accurate 
method for measuring RTTs.


Figure 5 visualizes the results of this whole experiment. We now try to conclude the various methods used based on these results with the help of our knowledge about the methods and underlying technologies. 


The RTT values collected from the P4 switches using the algorithm developed by Chen et al [2] are consistently lower than all the other methods. This pattern can be attributed to the fact that the calculation is being done on the switches instead of the nodes. This method is the true measure of the round-trip time of a network between two switches. Since the medium of communication is not known from a switch to the node in a network, the only common part of a traffic routing path between two nodes on different sites is the connection of a switch to another switch. 


The last method of calculating RTT was a Python script using Scapy. It was running on the application layer of the nodes in FABRIC. As expected, these values are consistently higher than the rest of the data. This behavior can be explained by the logic that the packets must pass through the kernel space to the Python program execution runtime for TCP acknowledgment in addition to the rest of the network.

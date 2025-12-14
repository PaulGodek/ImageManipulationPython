using UnityEngine;

public class BallMovement : MonoBehaviour
{

    public UDPReceive udpReceive;

    void Start()
    {
        
    }

    void Update()
    {
        string data = udpReceive.data; // Example : (255, 361, 50012) (x,y,area)
        data = data.Remove(0, 1);
        data = data.Remove(data.Length - 1, 1);

        string[] info = data.Split(',');

        float x = 5 - float.Parse(info[0]) / 100;
        float y = -2 + float.Parse(info[1]) / 100;
        float z = -10 + float.Parse(info[2]) / 1000;

        gameObject.transform.localPosition = new Vector3(x, y, z);
    }
}
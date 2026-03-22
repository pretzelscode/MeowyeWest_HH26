using Unity.Networking.Transport;
using UnityEngine;

#define PORT 9090

public class TCPClient : MonoBehaviour
{
    NetworkDriver driver;
    NetworkConnection connection;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        driver = NetworkDriver.Create();
        var endpoint = NetworkEndpoint.LoopbackIpv4.WithPort(PORT);
        connection = driver.Connect(endpoint);
    }

    void onDestroy(){
        driver.Dispose();
    }

    // Update is called once per frame
    void Update()
    {
        driver.ScheduleUpdate().Complete();

        if(!connection.isCreated){
            Debug.Log("No connection found");
            return;
        }   
    }
}

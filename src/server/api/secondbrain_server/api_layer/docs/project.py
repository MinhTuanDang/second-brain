from .basic_docs import add_api_code_docs, py_code, js_code, go_code

# Healthcheck endpoint
add_api_code_docs(
    "GET",
    "/healthcheck",
    py_code(
        """
from secondbrain import SecondBrainClient

secondbrain = SecondBrainClient(project_url='PROJECT_URL', api_key='PROJECT_TOKEN')

assert secondbrain.ping()
"""
    ),
    js_code(
        """
import { SecondBrainClient } from '@secondbrain/secondbrain';

const client = new SecondBrainClient(process.env.SECONDBRAIN_PROJECT_URL, process.env.SECONDBRAIN_API_KEY);

await client.ping();
"""
    ),
    go_code(
        """
import (
    "fmt"
    "log"

    "github.com/secondbrain-labs/secondbrain/src/client/secondbrain-go/core"
)

func main() {
    projectURL := "YOUR_PROJECT_URL"
    apiKey := "YOUR_API_KEY"
    // Initialize the client
    client, err := core.NewSecondBrainClient(
        projectURL,
        apiKey,
    )
    if err != nil {
        log.Fatalf("Failed to create client: %v", err)
    }

    // Ping the server
    if !client.Ping() {
        log.Fatal("Failed to connect to server")
    }
    fmt.Println("Successfully connected to server")
}
"""
    ),
)

# Project billing endpoint
add_api_code_docs(
    "GET",
    "/project/billing",
    py_code(
        """
from secondbrain import SecondBrainClient

secondbrain = SecondBrainClient(project_url='PROJECT_URL', api_key='PROJECT_TOKEN')

print(secondbrain.get_usage())
"""
    ),
    go_code(
        """
import (
    "fmt"
    "log"

    "github.com/secondbrain-labs/secondbrain/src/client/secondbrain-go/core"
)

func main() {
    projectURL := "YOUR_PROJECT_URL"
    apiKey := "YOUR_API_KEY"
    // Initialize the client
    client, err := core.NewSecondBrainClient(
        projectURL,
        apiKey,
    )
    if err != nil {
        log.Fatalf("Failed to create client: %v", err)
    }

    // Get usage
    usage, err := client.GetUsage()
    if err != nil {
        log.Fatalf("Failed to get usage: %v", err)
    }
    fmt.Printf("Usage: %v\n", usage)
}
"""
    ),
)

# Project profile config - POST
add_api_code_docs(
    "POST",
    "/project/profile_config",
    py_code(
        """
from secondbrain import SecondBrainClient

secondbrain = SecondBrainClient(project_url='PROJECT_URL', api_key='PROJECT_TOKEN')

secondbrain.update_config('your_profile_config')
"""
    ),
    js_code(
        """
import { SecondBrainClient } from '@secondbrain/secondbrain';

const client = new SecondBrainClient(process.env.SECONDBRAIN_PROJECT_URL, process.env.SECONDBRAIN_API_KEY);

await client.updateConfig('your_profile_config');
"""
    ),
    go_code(
        """
import (
    "fmt"
    "log"

    "github.com/secondbrain-labs/secondbrain/src/client/secondbrain-go/core"
)

func main() {
    projectURL := "YOUR_PROJECT_URL"
    apiKey := "YOUR_API_KEY"
    // Initialize the client
    client, err := core.NewSecondBrainClient(
        projectURL,
        apiKey,
    )
    if err != nil {
        log.Fatalf("Failed to create client: %v", err)
    }

    // Update config
    err = client.UpdateConfig("your_profile_config")
    if err != nil {
        log.Fatalf("Failed to update config: %v", err)
    }
    fmt.Println("Successfully updated config")
}
"""
    ),
)

# Project profile config - GET
add_api_code_docs(
    "GET",
    "/project/profile_config",
    py_code(
        """
from secondbrain import SecondBrainClient

secondbrain = SecondBrainClient(project_url='PROJECT_URL', api_key='PROJECT_TOKEN')

config = secondbrain.get_config()
"""
    ),
    js_code(
        """
import { SecondBrainClient } from '@secondbrain/secondbrain';

const client = new SecondBrainClient(process.env.SECONDBRAIN_PROJECT_URL, process.env.SECONDBRAIN_API_KEY);

const config = await client.getConfig();
"""
    ),
    go_code(
        """
import (
    "fmt"
    "log"

    "github.com/secondbrain-labs/secondbrain/src/client/secondbrain-go/core"
)

func main() {
    projectURL := "YOUR_PROJECT_URL"
    apiKey := "YOUR_API_KEY"
    // Initialize the client
    client, err := core.NewSecondBrainClient(
        projectURL,
        apiKey,
    )
    if err != nil {
        log.Fatalf("Failed to create client: %v", err)
    }

    // Get config
    config, err := client.GetConfig()
    if err != nil {
        log.Fatalf("Failed to get config: %v", err)
    }
    fmt.Printf("Config: %s\n", config)
}
"""
    ),
)

# Project users endpoint
add_api_code_docs(
    "GET",
    "/project/users",
    py_code(
        """
from secondbrain import SecondBrainClient

secondbrain = SecondBrainClient(project_url='PROJECT_URL', api_key='PROJECT_TOKEN')

users = secondbrain.get_all_users(search="", order_by="updated_at", order_desc=True, limit=10, offset=0)
"""
    ),
    go_code(
        """
import (
    "fmt"
    "log"

    "github.com/secondbrain-labs/secondbrain/src/client/secondbrain-go/core"
)

func main() {
    projectURL := "YOUR_PROJECT_URL"
    apiKey := "YOUR_API_KEY"
    // Initialize the client
    client, err := core.NewSecondBrainClient(
        projectURL,
        apiKey,
    )
    if err != nil {
        log.Fatalf("Failed to create client: %v", err)
    }

    // Get all users
    users, err := client.GetAllUsers("", "updated_at", true, 10, 0)
    if err != nil {
        log.Fatalf("Failed to get all users: %v", err)
    }
    fmt.Printf("Found %d users\n", len(users))
}
"""
    ),
)

# Project usage endpoint
add_api_code_docs(
    "GET",
    "/project/usage",
    py_code(
        """
from secondbrain import SecondBrainClient

secondbrain = SecondBrainClient(project_url='PROJECT_URL', api_key='PROJECT_TOKEN')

usage = secondbrain.get_daily_usage(days=7)
"""
    ),
    go_code(
        """
import (
    "fmt"
    "log"

    "github.com/secondbrain-labs/secondbrain/src/client/secondbrain-go/core"
)

func main() {
    projectURL := "YOUR_PROJECT_URL"
    apiKey := "YOUR_API_KEY"
    // Initialize the client
    client, err := core.NewSecondBrainClient(
        projectURL,
        apiKey,
    )
    if err != nil {
        log.Fatalf("Failed to create client: %v", err)
    }

    // Get daily usage
    usage, err := client.GetDailyUsage(7)
    if err != nil {
        log.Fatalf("Failed to get daily usage: %v", err)
    }
    fmt.Printf("Usage: %v\n", usage)
}
"""
    ),
)

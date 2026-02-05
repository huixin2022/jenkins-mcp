#!/usr/bin/env python
"""
Standalone entry point for mcp-jenkins MCP server.
Usage: python run_server.py --jenkins-url=xxx --jenkins-username=xxx --jenkins-password=xxx
"""
import sys
sys.path.insert(0, 'src')

from mcp_jenkins import main

if __name__ == '__main__':
    main()


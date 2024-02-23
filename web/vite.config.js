const path = require('path');
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
    resolve: {
        alias: {
            src: path.resolve(__dirname, './src'),
            service: path.resolve(__dirname, './src/service'),
            component: path.resolve(__dirname, './src/component'),
            style: path.resolve(__dirname, './src/style')
        }
    },
    server: {
        host: '0.0.0.0',
        port: 3000,
        hmr: {
            host: process.env.VITE_DOMAIN,
            clientPort: 443,
            protocol: 'wss'
        }
    },
    plugins: [
        react({
            fastRefresh: process.env.NODE_ENV !== 'test'
        })
    ],
    test: {
        globals: true,
        environment: 'jsdom',
        setupFiles: ['./src/vitest.setup.js']
    },
    css: {
        preprocessorOptions: {
            less: {
                modifyVars: {
                    'primary-color': '@blue-6'
                },
                javascriptEnabled: true
            }
        }
    }
});

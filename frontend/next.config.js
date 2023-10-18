/** @type {import('next').NextConfig} */
const nextConfig = {
    async rewrites() {
        return [{
            source: '/backend/:path*',
            destination: 'http://localhost:8000/:path*'
        }]
    }
}

module.exports = nextConfig

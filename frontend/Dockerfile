# Use official Node.js runtime as base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Install yarn globally (if not already available)
RUN corepack enable

# Copy package files first for better caching
COPY package.json yarn.lock* ./

# Install dependencies with yarn
RUN yarn install --frozen-lockfile --production=false

# Copy application code
COPY . .

# Build the Next.js application
RUN yarn build

# Create non-root user for security
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

# Change ownership of the app directory
RUN chown -R nextjs:nodejs /app
USER nextjs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:3000 || exit 1

# Start the application
CMD ["yarn", "start"]
